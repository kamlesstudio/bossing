from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

class BlackBusiness(models.Model):
    yvonne = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(blank=True)
    id = models.AutoField(primary_key=True)
    cleaned = models.CharField(max_length=30, null=True, blank=True)
    valid = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=13000, null=True, blank=True)
    website = models.CharField(max_length=10000, null=True, blank=True)
    title = models.CharField(max_length=10300, null=True, blank=True)
    tags = models.CharField(max_length=13000, null=True, blank=True)
    phone = models.CharField(max_length=13000, null=True, blank=True)
    operation_hours = models.CharField(max_length=10000, null=True, blank=True)
    latitude = models.FloatField(max_length=5000, null=True, blank=True)
    longitude = models.FloatField(max_length=5500, null=True, blank=True)
    email = models.CharField(max_length=5000, null=True, blank=True)
    description = models.CharField(max_length=20000, null=True, blank=True)
    address = models.CharField(max_length=30000, null=True, blank=True)
    source = models.CharField(max_length=20000, null=True, blank=True)
    county = models.CharField(max_length=3000, null=True, blank=True)
    country_code = models.CharField(max_length=3000, null=True, blank=True)
    black_owned = models.CharField(max_length=3000, null=True, blank=True)
    category2 = models.CharField(max_length=30000, null=True, blank=True)
    yelp_link = models.CharField(max_length=30000, null=True, blank=True)
    image = models.CharField(max_length=200000, null=True, blank=True)
    social_media = models.CharField(max_length=20000, null=True, blank=True)
    notes = models.CharField(max_length=20000, null=True, blank=True)
    keyword = models.CharField(max_length=20000, null=True, blank=True)

    # RATING FIELDS (RATING COUNT AND RATING TOTAL)
    rating_total = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    
    def get_rating_avg(self):
      if int(self.rating_count) < 1:
          rating = 0
      else:
          rating = int(self.rating_total)/self.rating_count
        
      return rating

    def valid_cleaned(self):
        valid_business = BlackBusiness.objects.filter(valid__icontains="Y").order_by('id')
        return valid_business

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.title or ''
