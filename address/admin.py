from django.contrib import admin
from models import BillingAddress, ShippingAddress


class BillingAddressAdmin(admin.ModelAdmin):

    change_list_filter_template = "admin/filter_listing.html"
    search_fields = ('email', 'id')
    list_filter = ('status', )
    list_display = ('email', '__str__', 'status')


class ShippingAddressAdmin(admin.ModelAdmin):

    search_fields = ('email', 'id')
    list_filter = ('status', )
    list_display = ('email', '__str__', 'status')

admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
