"""NBAEncyclopedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy, reverse
from NBAE import views

app_name = 'NBAE'

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^records/$',views.MultipleRecordListView.as_view(), name='record_list'),
    url(r'^player/record/view/(?P<pk>\d+)$', views.PlayerRecordDetailView.as_view(), name='playerrecord_detail'),
    url(r'^team/record/view/(?P<pk>\d+)$', views.TeamRecordDetailView.as_view(), name='teamrecord_detail'),
    url(r'^season/record/view/(?P<pk>\d+)$', views.SeasonRecordDetailView.as_view(), name='seasonrecord_detail'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^record/create/$', views.create_view, name='create'),
    url(r'^records/drafts/$', views.DraftListView.as_view(), name='record_draft_list'),
    url(r'^records/recordlist/$', views.MultipleRecordListView.as_view(), name='multiple_record_list'),
    url(r'^record/createplayer/$', views.CreatePlayerRecordView.as_view(),name='createplayer'),
    url(r'^record/createteam/$', views.CreateTeamRecordView.as_view(), name='createteam'),
    url(r'^record/createseason/$', views.CreateSeasonRecordView.as_view(), name='createseason'),
    url(r'^player/record/delete/confirm/(?P<pk>\d+)', views.playerconfirm_deleteview, name='confirmplayer'),
    url(r'^team/record/delete/confirm/(?P<pk>\d+)', views.teamconfirm_deleteview, name='confirmteam'),
    url(r'^season/record/delete/confirm/(?P<pk>\d+)', views.seasonconfirm_deleteview, name='confirmseason'),
    url(r'^player/record/update/(?P<pk>\d+)$', views.PlayerRecordUpdateView.as_view(), name='updateplayer'),
    url(r'^team/record/update/(?P<pk>\d+)$', views.TeamRecordUpdateView.as_view(), name='updateteam'),
    url(r'^season/record/update/(?P<pk>\d+)$', views.SeasonRecordUpdateView.as_view(), name='updateseason'),
    url(r'^player/record/delete/(?P<pk>\d+)$', views.delete_playerrecord, name='deleteplayer'),
    url(r'^team/record/delete/(?P<pk>\d+)$', views.delete_teamrecord, name='deleteteam'),
    url(r'^season/record/delete/(?P<pk>\d+)$', views.delete_seasonrecord, name='deleteseason'),
    url(r'^player/record/(?P<pk>\d+)/publish/$', views.playerrecord_publish, name='playerrecord_publish'),
    url(r'^team/record/(?P<pk>\d+)/publish/$', views.teamrecord_publish, name='teamrecord_publish'),
    url(r'^season/record/(?P<pk>\d+)/publish/$', views.seasonrecord_publish, name='seasonrecord_publish'),
    url(r'^profile/$', views.profile_view, name='profile_view'),
    url(r'^profile/edit$', views.edit_profile, name='profile_edit'),
    url(r'^searchresults$', views.search_results, name='search_results'),
    url(r'^record/(?P<pk>\d+)/comment/$', views.add_comment_to_record, name='add_comment_to_record'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^records/sort-by/results', views.sort_by_records, name='sort-by-results'),
    url(r'^records/sort-by', views.sort_view, name='sort-view')
]
