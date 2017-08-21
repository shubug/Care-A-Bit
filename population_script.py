import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'care_a_bit.settings')

import django
django.setup()

from django.contrib.auth.models import User
from donor.models import DonorProfile

def populate():
    user = User.objects.filter(username='ankit')[0]
    dp = DonorProfile.objects.get_or_create(user=user)[0]
    dp.save()
    print "Ending population script"


# Start Execution here!
if __name__ == '__main__':
    print "Starting population script"
    populate()