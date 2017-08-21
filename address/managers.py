from django.db import models


class ActiveAddressManager(models.Manager):
    def get_queryset(self):
        return super(ActiveAddressManager, self).get_queryset().filter(status='Active')