from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class NgoCategory(models.Model):
    domain = models.CharField(max_length=255, unique=True)
    num_of_contrib = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #self.slug = slugify(self.name)
        self.slug = slugify(self.domain)
        super(NgoCategory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.domain
   
    class Meta:
        verbose_name = 'Ngocategory'
        verbose_name_plural = 'NgoCategories'


class Ngo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    link = models.URLField(blank=True)
    category = models.ForeignKey(NgoCategory, null=True, blank=True)
    total_contrib = models.IntegerField(default=0)
    last_contrib = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(default='xxxngoxxx')
    # Need to add address here as FK

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Ngo'
        verbose_name_plural = 'Ngos'