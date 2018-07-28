import datetime
from django.db import models
from Accounts.models import Usernames
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    title           = models.CharField(max_length=120)
    user            = models.ForeignKey(User,
                        on_delete=models.CASCADE)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.IntegerField(default=0)
    image           = models.ImageField(upload_to='uploads/', null=True, blank=True)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now=True)
    max_duration    = models.IntegerField(default=0)
    duration        = models.IntegerField()
    choice = (
    ('GA','Gardening'),
    ('CO','Construction'),
    ('MA','Maintenacne')
    ('TA','Travel'),
    )
    category        = models.CharField(choices = choice )
    # user, duration (preferred),max_duration

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

#Product condition
class ProductCondition(models.Model):
        warranty = models.BooleanField(default=False)
        # warranty_time
        level = (
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five')
        )
        tear_wear = models.PositiveIntegerField(choices=(level))
        insurance_covered = models.BooleanField(default=False)
        purchase_date = models.DateTimeField(default=False)
        additional_info = models.TextField()

# class Category(models.Model):
#     category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.category
#
# class Subcategory(models.Model):
#     subcategory = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.subcategory
