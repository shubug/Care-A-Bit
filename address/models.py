import re

from django.conf import settings
from django.core import exceptions
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy
#from order.models import Order
import hashlib
from django.utils.encoding import smart_str

#from fields import UppercaseCharField
from cities_light_proxy.models import MyRegion, MyCountry
from managers import ActiveAddressManager
from django.db.models import Q
import copy
import sys


@python_2_unicode_compatible
class AbstractAddress(models.Model):

    """
    Superclass address object

    This is subclassed and extended to provide models for
    shipping and billing addresses.
    """

    # user = models.ForeignKey(Customer, null=True)
    email = models.EmailField(blank=True)

    MR, MISS, MRS, MS, DR = ('Mr', 'Miss', 'Mrs', 'Ms', 'Dr')
    TITLE_CHOICES = (
        (MR, "Mr"),
        (MISS, "Miss"),
        (MRS, "Mrs"),
        (MS, "Ms"),
        (DR, "Dr"),
    )

    ACT, INACT, DEL = ('Active', 'Inactive', 'Deleted')
    STATUS_CHOICES = (
        (ACT, "Active"),
        (INACT, "Inactive"),
        (DEL, "Deleted"),
    )

    POSTCODE_REQUIRED = 'postcode' in settings.REQUIRED_ADDRESS_FIELDS

    title = models.CharField(
        pgettext_lazy("Treatment Pronouns for the customer", "Title"),
        max_length=64, choices=TITLE_CHOICES, blank=True, null=True)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    country = models.ForeignKey(MyCountry, null=True, blank=True)

    region = models.ForeignKey(MyRegion, null=True, blank=True)

    city = models.CharField("City", max_length=150, null=True, blank=True)
    
    postcode = CharField(max_length=64)
    # postcode = UppercaseCharField(
    #     "Post/Zip-code", max_length=64)

    # We use quite a few lines of an address as they are often quite long and
    # it's easier to just hide the unnecessary ones than add extra ones.
    line1 = models.CharField(max_length=255, blank=True, null=True)
    line2 = models.CharField(
        "Second line of address", max_length=255, blank=True, null=True)

    date_created = models.DateTimeField(
        "Date Created", auto_now_add=True, null=True)

    date_updated = models.DateTimeField(
        "Date Updated", auto_now=True, null=True)

    phone_number = models.CharField(
        ("Phone number"),
        max_length=50,
        help_text="In case we need to call you",
        blank=True, null=True)

    migrated_from_orders = models.BooleanField(default=False)

    address_hash = models.CharField(max_length=50, blank=False, null=False)

    status = models.CharField(max_length=20,
                              default="Active", choices=STATUS_CHOICES)

    def __str__(self):
        address_str = self.first_name + ' '
        if self.last_name:
            address_str += self.last_name
        address_str += '\n' + \
            self.line1 + '\n'
        if self.line2:
            address_str += self.line2 + '\n'
        if self.city:
            address_str += self.city + ' '
        if self.region:
            address_str += unicode(self.region) + ' '
        if self.postcode:
            address_str += self.postcode + '\n'
        address_str += unicode(self.country)
        if self.phone_number:
            address_str += '\n' + self.phone_number
        return address_str
        # return "%s %s - %s" % (self.title, self.first_name, self.postcode)

    def get_address_hash(self):
        # Note: This is a pretty dumb de-dup algo for handling
        # address migrations for duplicates. We need a better
        # algo at some point to compute de-duplication
        region_str = ''
        try:
            region_str = self.region.name
        except:
            pass
        country_str = ''
        try:
            country_str = self.country.code2
        except:
            pass
        add_string = "%s-%s-%s-%s-%s" % (
            self.email, country_str, self.first_name, region_str, self.postcode)
        add_string = smart_str(add_string, encoding='ascii', errors='ignore')
        add_hash = hashlib.md5()
        add_hash.update(add_string)
        return add_hash.hexdigest()

    class Meta:
        abstract = True
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def clean(self):
        # Strip all whitespace
        for field in ['first_name', 'last_name', 'line1', 'line2',
                      'postcode']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

        # Ensure postcodes are valid for country
        self.ensure_postcode_is_valid_for_country()

    def ensure_postcode_is_valid_for_country(self):
        """
        Validate postcode given the country
        """
        if not self.postcode and self.POSTCODE_REQUIRED and self.country_id:
            country_code = self.country.code2
            regex = settings.POSTCODES_REGEX.get(country_code, None)
            if regex:
                msg = "Addresses in %(country)s require a valid postcode" \
                    % {'country': self.country}
                raise exceptions.ValidationError(msg)

        if self.postcode and self.country_id:
            # Ensure postcodes are always uppercase
            postcode = self.postcode.upper().replace(' ', '')
            country_code = self.country.code2
            regex = settings.POSTCODES_REGEX.get(country_code, None)

            # Validate postcode against regex for the country if available
            if regex and not re.match(regex, postcode):
                msg = "The postcode '%(postcode)s' is not valid " \
                        "for %(country)s" \
                    % {'postcode': self.postcode,
                       'country': self.country}
                raise exceptions.ValidationError(
                    {'postcode': [msg]})

    def delete(self, *args, **kwargs):
        if self.order_set.all():  # only if address is linked to an order
            self.save(delete=True)
        else:  # Normal Delete
            super(AbstractAddress, self).delete(*args, **kwargs)

    def save(self, delete=None, *args, **kwargs):
        if self.status != 'Active':
            self.is_default = False
        if self.pk is not None:  # Edit
            if self.order_set.all():  # only if address is linked to an order
                if delete:
                    self.status = 'Deleted'
                    self.is_default = False
                    super(AbstractAddress, self).save(*args, **kwargs)
                else:
                    new_address = create_new_address(self)
                    if isinstance(self, BillingAddress):
                        BillingAddress.objects.filter(
                            id=self.id).update(status='Inactive', is_default = False)
            else:  # Normal Edit
                super(AbstractAddress, self).save(*args, **kwargs)
        else:  # Normal Save
            super(AbstractAddress, self).save(*args, **kwargs)


def create_new_address(address):
    new_address = copy.deepcopy(address)
    new_address.status = "Active"
    new_address.pk = None
    new_address.save()
    return new_address


class ShippingAddress(AbstractAddress):

    """
    A shipping address.
    """

    notes = models.TextField(
        blank=True, verbose_name='Instructions',
        help_text="Tell us anything we should know when delivering "
                    "your order.")
    is_default = models.BooleanField(default=False)

    admin_objects = models.Manager()
    objects = ActiveAddressManager()

    class Meta:
        app_label = 'address'
        verbose_name = "Shipping address"
        verbose_name_plural = "Shipping addresses"

    def save(self, *args, **kwargs):
        if self.is_default:
            try:
                prev_default = ShippingAddress.objects.get(
                    email=self.email, is_default=True)
                prev_default.is_default = False
                prev_default.save()
            except:
                print "Object Does Not Exist"
        address_hash = self.get_address_hash()
        self.address_hash = address_hash
        super(ShippingAddress, self).save(*args, **kwargs)


class BillingAddress(AbstractAddress):

    """
    A billing address.
    """

    is_default = models.BooleanField(default=False)

    admin_objects = models.Manager()
    objects = ActiveAddressManager()

    class Meta:
        app_label = 'address'
        verbose_name = "Billing address"
        verbose_name_plural = "Billing addresses"

    def save(self, *args, **kwargs):
        if self.is_default:
            try:
                prev_default = BillingAddress.objects.get(
                    email=self.email, is_default=True)
                prev_default.is_default = False
                prev_default.save()
            except:
                print "Object Does Not Exist"
        address_hash = self.get_address_hash()
        self.address_hash = address_hash
        super(BillingAddress, self).save(*args, **kwargs)