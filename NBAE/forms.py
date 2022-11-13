from django import forms

from .models import Comment, User, Profile, PlayerRecords, TeamRecords, SeasonRecords,Records
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('record', 'text',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
        exclude = ('record',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        db_table = 'auth_user'
        fields = ['username', 'password', 'email']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        try:
            match = User.objects.get(password=password)
        except User.DoesNotExist:
            return password

        raise forms.ValidationError('This password is already in use.')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        db_table = 'NBAE_profile'
        fields = ['user', 'first_name', 'last_name', 'age', 'hometown', 'bio', 'image']
        exclude = ('user',)

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        db_table = 'NBAE_profile'
        fields = ['user', 'first_name', 'last_name', 'age', 'hometown', 'bio', 'image']
        exclude = ('user',)


class PlayerRecordForm(forms.ModelForm):



    def save(self, commit=True):
        obj = super(PlayerRecordForm, self).save(commit=False)
        obj.type = str("Player")
        obj.save()


    class Meta:
        model = PlayerRecords
        fields = ('author','name','type','player_dob', 'player_birthplace', 'player_nationality',
                  'player_highschool', 'player_college', 'player_currentteam', 'player_allteams',
                  'player_bio', 'player_profile', 'player_accolades', 'player_references', 'image')
        exclude = ('type', 'author')
        labels = {
            "player_dob": "Date of Birth",
            "player_birthplace": "Birth Place",
            "player_nationality": "Nationality",
            "player_highschool": "High School",
            "player_college": "Player College",
            "player_currentteam": "Current Team",
            "player_allteams": "All Teams",
            "player_bio": "Biography",
            "player_profile": "Profile",
            "player_accolades": "Accolades",
            "player_references": "References"
        }
class TeamRecordForm(forms.ModelForm):

    def save(self, commit=True):
        obj = super(TeamRecordForm, self).save(commit=False)
        obj.type = str("Team")
        obj.save()

    class Meta:
        model = TeamRecords
        fields = ('author','name','type', 'team_conference', 'team_division', 'team_founded',
                  'team_arena', 'team_location', 'team_gm', 'team_coach', 'team_owner',
                  'team_accolades', 'team_roster', 'team_bio', 'team_reference', 'image')
        exclude = ('type', 'author')
        labels = {
            "team_conference": "Conference",
            "team_division": "Division",
            "team_founded": "Founded",
            "team_arena": "Arena",
            "team_location": "Location",
            "team_gm": "General Manager",
            "team_coach": "Coach",
            "team_owner": "Owner",
            "team_accolades": "Accolades",
            "team_roster": "Current Roster",
            "team_bio": "Biography",
            "team_reference": "References"
        }

class SeasonRecordForm(forms.ModelForm):

    def save(self, commit=True):
        obj = super(SeasonRecordForm, self).save(commit=False)
        obj.type = str("Season")
        obj.save()

    class Meta:
        model = SeasonRecords
        fields = ('author','name','type','season_league', 'season_duration', 'season_not',
                  'season_allteams','season_mvp', 'season_roy', 'season_doy', 'season_smoy',
                  'season_mip', 'season_coy', 'season_champion', 'season_fmvp', 'season_bio', 'image')
        exclude = ('type', 'author')
        labels = {
            "season_league": "League",
            "season_duration": "Duration",
            "season_not": "Number of Teams",
            "season_allteams": "NBA Teams",
            "season_mvp": "Most Valuable Player(MVP)",
            "season_roy": "Rookie of the Year(ROY)",
            "season_doy": "Defensive Player of the Year(DOY)",
            "season_mip": "Most Improved Player(MIP)",
            "season_coy": "Coach of the Year(COY)",
            "season_champion": "NBA Champions",
            "season_fmvp": "NBA Finals MVP",
            "season_smoy": "Sixth Man of Injury",
            "season_bio": "Biography",


        }
class RecordSortForm(forms.ModelForm):

    class Meta:
        model = Records
        fields = ['author', 'published_date', 'is_verified', 'type']

    def __init__(self):
        super(RecordSortForm, self).__init__()
        self.fields['author'].queryset = self.fields['author'].queryset.order_by('author')