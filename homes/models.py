from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


# Create your models here.
# class dataUser(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=5)
#     phoneNum = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     userLevel = models.BooleanField(default=False)


class kilidUser(models.Model):
    REQUIRED_FIELDS = ('user',)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phoneNum = models.CharField(max_length=50)
    isManager = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        kilidUser.objects.create(user=instance, isManager=False)


# @receiver(post_save, sender=User)
# def save_kilidUser(sender, instance, **kwargs):
#     instance.kilidUser.save()


class Image(models.Model):
    image = models.CharField(max_length=500)

    # @property
    # def get_photo_url(self):
    #     return '/static/images/%s.jpg' % self.image
    # # related_house = models.OneToOneField(Housing, on_delete=models.CASCADE, null=True)


class Housing(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.CharField(max_length=50)
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    parkings = models.IntegerField()
    locality = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    # pic =  models.CharField(max_length=50)
    estate = models.CharField(max_length=50)
    star = models.BooleanField(default=False)
    # bookmark = models.BooleanField(default=False)


class Bookmark(models.Model):
    user = models.ForeignKey(kilidUser, on_delete=models.CASCADE, null=True)
    house = models.ForeignKey(Housing, on_delete=models.CASCADE, null=True)





class Comment(models.Model):
    comment = models.CharField(max_length=200)
    houseID = models.CharField(max_length=50)
    # housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    time = models.DateTimeField()



