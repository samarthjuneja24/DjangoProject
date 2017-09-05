from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    profile_pic=models.ImageField(upload_to='profilepics/%Y/%m/%d/',default='\LoginPage\images\default.jpg')
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

class Video(models.Model):
    username=models.ForeignKey(UserProfile,on_delete=models.CASCADE,default="",related_name='uservideos')
    video=models.FileField(upload_to='videos/%Y/%m/%d/',default='')
    videotitle=models.CharField(max_length=100)
    likes=models.PositiveIntegerField(default=0)
    dislikes=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.video.url

    def delete(self):
        self.video.delete()
        super(Video,self).delete()