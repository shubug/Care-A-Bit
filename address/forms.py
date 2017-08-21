from django.forms import ModelForm
from address.models import ShippingAddress, BillingAddress


class ShippingAddressForm(ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['title', 'first_name', 'last_name', 'country', 'region',
                  'city', 'postcode', 'line1', 'line2', 'line3',
                  'phone_number', 'is_default']


class BillingAddressForm(ModelForm):

    class Meta:
        model = BillingAddress
        fields = ['title', 'first_name', 'last_name', 'country', 'region',
                  'city', 'postcode', 'line1', 'line2', 'line3',
                  'phone_number', 'is_default']