from django.contrib import admin
from donor.models import DonorProfile

class DonorProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'picture', 'is_active', 'total_donation')

#admin.site.register(DonorProfile)
admin.site.register(DonorProfile, DonorProfileAdmin)
