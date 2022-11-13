from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
# Create your models here.


# ADD PICTURES!!!!!!!!!!!!!!
# Report will be inside of record
class DeletedRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    record = models.CharField(max_length=100)



class Comment(models.Model):

    record = models.ForeignKey('NBAE.Records', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("record_list")

    def __str__(self):
        return self.name

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    hometown = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)

    def __str__(self):
        self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Records(models.Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=False, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='record_image', blank=True)

class SeasonRecords(Records):

    season_league = models.CharField(max_length=50, null=True, blank=True)
    season_duration = models.CharField(max_length=50, null=True, blank=True)
    season_not = models.CharField(max_length=10, null=True, blank=True)
    season_allteams = models.TextField(max_length=500, null=True, blank=True)
    season_mvp = models.CharField(max_length=50, null=True, blank=True)
    season_roy = models.CharField(max_length=50, null=True, blank=True)
    season_doy = models.CharField(max_length=50, null=True, blank=True)
    season_smoy = models.CharField(max_length=50, null=True, blank=True)
    season_mip = models.CharField(max_length=50, null=True, blank=True)
    season_coy = models.CharField(max_length=50, null=True, blank=True)
    season_champion = models.CharField(max_length=50, null=True, blank=True)
    season_fmvp = models.CharField(max_length=50, null=True, blank=True)
    season_bio = models.TextField(max_length=1000, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("NBAE:seasonrecord_detail",kwargs={'pk':self.pk})

class TeamRecords(Records):

    team_conference = models.CharField(max_length=50, null=True, blank=True)
    team_division = models.CharField(max_length=50, null=True, blank=True)
    team_founded = models.DateField(null=True, blank=True)
    team_arena = models.CharField(max_length=50, null=True, blank=True)
    team_location = models.CharField(max_length=50, null=True, blank=True)
    team_gm = models.CharField(max_length=50, null=True, blank=True)
    team_coach = models.CharField(max_length=50, null=True, blank=True)
    team_owner = models.CharField(max_length=50, null=True, blank=True)
    team_accolades = models.TextField(max_length=500, blank=True, null=True)
    team_roster = models.TextField(max_length=500, blank=True, null=True)
    team_bio = models.TextField(max_length=1000, blank=True, null=True)
    team_reference = models.TextField(max_length=500, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("NBAE:teamrecord_detail",kwargs={'pk':self.pk})




class PlayerRecords(Records):

    player_dob = models.DateField(blank=True, null=True)
    player_birthplace = models.CharField(max_length=30, blank=True, null=True)
    player_nationality = models.CharField(max_length=30, blank=True, null=True)
    player_highschool = models.CharField(max_length=40, blank=True, null=True)
    player_college = models.CharField(max_length=40, blank=True, null=True)
    player_currentteam = models.CharField(max_length=30, blank=True, null=True)
    player_allteams = models.CharField(max_length=40, blank=True, null=True)
    player_bio = models.TextField(max_length=1000, blank=True, null=True)
    player_profile = models.TextField(max_length=500, blank=True, null=True)
    player_accolades = models.TextField(max_length=500, blank=True, null=True)
    player_references = models.TextField(max_length=500, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("NBAE:playerrecord_detail",kwargs={'pk':self.pk})

class CarouselImageModel(models.Model):
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
