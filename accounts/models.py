from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# From https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone


# Create user profile, which will be  one-to-one use User model
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    avatar = CloudinaryField('avatar', default='default.jpg',)
    # user_image = models.ImageField(
    #     default='default.jpg', upload_to='profile_pics')
    user_p_pagination = models.IntegerField(default=15, null=True)
    user_b_pagination = models.IntegerField(default=15, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# This will create new profile when you create new user = post_save triggers when model (User) is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# This will save profile when you update user
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()
