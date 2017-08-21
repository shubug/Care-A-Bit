from django.contrib import admin
from ngo.models import Ngo, NgoCategory

class NgoAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'total_contrib', 'last_contrib')

class NgoCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ngo, NgoAdmin)
admin.site.register(NgoCategory)

