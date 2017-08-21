from django.db import models
from django.contrib.auth.models import User

class DonorProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='donor_profiles', blank=True)
    #dob = models.DateField(max_length=8)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # address = models.ForeignKey(Address)
    total_donation = models.IntegerField(default = 0)
    # preferences_of_ngos = 

    def __unicode__(self):
        return self.user.username