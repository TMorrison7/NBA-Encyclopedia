from django.contrib import admin
from .models import CarouselImageModel, PlayerRecords, Profile, Comment, Records, TeamRecords, SeasonRecords, User
# Register your models here.

admin.site.register(Records)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(PlayerRecords)
admin.site.register(TeamRecords)
admin.site.register(SeasonRecords)
admin.site.register(CarouselImageModel)