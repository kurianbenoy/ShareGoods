from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usernames(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    aadhar_no = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)],default=0)
    location = models.CharField(max_length=100,default="")
    is_activate = models.BooleanField(default=False,)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    image           = models.ImageField(upload_to='uploads/', null=True, blank=True)
    def get_aadharno(self):
        return self.Aadhar_no

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Usernames.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,**kwargs):
#     instance.User.save()

class Rating(models.Model):
    ratings =  (
    (1,'One'),
    (2,'Two'),
    (3,'Three'),
    (4,'Four'),
    (5,'Five')
    )
    rate = models.PositiveIntegerField(choices=ratings)
    # reviewer = models.ForeignKey(Usernames,
    #     on_delete=models.CASCADE)

class Review(models.Model):
    review = models.TextField()
    # reviewer = models.ForeignKey(Usernames,
    #     on_delete=models.CASCADE)
