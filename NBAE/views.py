from django.contrib import messagesfrom django.http import HttpResponseRedirectfrom django.shortcuts import renderfrom django.shortcuts import redirect, get_object_or_404from NBAE.forms import CommentForm, PlayerRecordForm, UserForm,UpdateProfileForm,ProfileForm, TeamRecordForm, SeasonRecordForm, RecordSortFormfrom django.urls import reverse_lazy, reversefrom NBAE.models import Comment, DeletedRecord, Records, User, PlayerRecords, TeamRecords, SeasonRecords, Profile, CarouselImageModelfrom django.views.generic import (TemplateView,ListView,                                  DetailView,CreateView,                                  UpdateView,DeleteView, View)from django.contrib.auth.mixins import LoginRequiredMixinfrom django.contrib.auth.decorators import login_requiredfrom django.core.paginator import Paginator, EmptyPage, PageNotAnIntegerfrom django.contrib.auth.forms import AuthenticationFormfrom django.db.models import Qfrom django.contrib import authid = 1list = []list2 = []# dclass PlayerRecordDetailView(DetailView):    model = PlayerRecordsclass TeamRecordDetailView(DetailView):    model = TeamRecordsclass SeasonRecordDetailView(DetailView):    model = SeasonRecordsclass MultipleRecordListView(TemplateView):    login_url = '/login/'    template_name = 'Encyclopedia/Record/records_list.html'    def get_context_data(self):        user_name = self.request.user.username        context = super(MultipleRecordListView, self).get_context_data()        context['PlayerRecords'] = PlayerRecords.objects.filter(is_draft=False, author__username=user_name).order_by('-published_date')        context['TeamRecords'] = TeamRecords.objects.filter(is_draft=False, author__username=user_name).order_by('-published_date')        context['SeasonRecords'] = SeasonRecords.objects.filter(is_draft=False, author__username=user_name).order_by('-published_date')        return contextclass CreatePlayerRecordView(LoginRequiredMixin, CreateView):    login_url = '/login/'    redirect_field_name = 'Encyclopedia/Record/records_list.html'    model = PlayerRecords    form_class = PlayerRecordForm    def get_success_url(self):        return reverse('NBAE:record_draft_list')    def post(self, request, *args, **kwargs):        self.object = None        form_class = self.get_form_class()        form = self.get_form(form_class)        form.instance.author = request.user        if form.is_valid():            return self.form_valid(form)        else:            return self.form_invalid(form)class CreateTeamRecordView(LoginRequiredMixin, CreateView):    login_url = '/login/'    redirect_field_name = 'Encyclopedia/Record/records_list.html'    model = TeamRecords    form_class = TeamRecordForm    def get_success_url(self):        return reverse('NBAE:record_draft_list')    def post(self, request, *args, **kwargs):        self.object = None        form_class = self.get_form_class()        form = self.get_form(form_class)        form.instance.author = request.user        if form.is_valid():            return self.form_valid(form)        else:            return self.form_invalid(form)class CreateSeasonRecordView(LoginRequiredMixin, CreateView):    login_url = '/login/'    redirect_field_name = 'Encyclopedia/Record/records_list.html'    model = SeasonRecords    form_class = SeasonRecordForm    def get_success_url(self):        return reverse('NBAE:record_draft_list')    def post(self, request, *args, **kwargs):        self.object = None        form_class = self.get_form_class()        form = self.get_form(form_class)        form.instance.author = request.user        if form.is_valid():            return self.form_valid(form)        else:            return self.form_invalid(form)class PlayerRecordUpdateView(LoginRequiredMixin, UpdateView):    login_url = '/login/'    redirect_field_name = 'NBAE/playerrecord_detail.html'    form_class = PlayerRecordForm    model = PlayerRecords    def get_success_url(self):        return reverse('NBAE:record_draft_list')class TeamRecordUpdateView(LoginRequiredMixin, UpdateView):    login_url = '/login/'    redirect_field_name = 'NBAE/teamrecord_detail.html'    form_class = TeamRecordForm    model = TeamRecords    def get_success_url(self):        return reverse('NBAE:record_draft_list')class SeasonRecordUpdateView(LoginRequiredMixin, UpdateView):    login_url = '/login/'    redirect_field_name = 'NBAE/seasonrecord_detail.html'    form_class = SeasonRecordForm    model = SeasonRecords    def get_success_url(self):        return reverse('NBAE:record_draft_list')class ProfileUpdateView(LoginRequiredMixin, UpdateView):    login_url = '/login/'    redirect_field_name = 'NBAE/profile_detail.html'    form_class = ProfileForm    model = Profileclass DraftListView(LoginRequiredMixin, TemplateView):    login_url = '/login/'    template_name = 'Encyclopedia/Record/records_list.html'    def get_context_data(self):        user_name = self.request.user.username        context = super(DraftListView, self).get_context_data()        context['PlayerRecords'] = PlayerRecords.objects.filter(is_draft=True, author__username=user_name).order_by('-created_date')        context['TeamRecords'] = TeamRecords.objects.filter(is_draft=True, author__username=user_name).order_by('-created_date')        context['SeasonRecords'] = SeasonRecords.objects.filter(is_draft=True, author__username=user_name).order_by('-created_date')        return contextdef home_view(request):    queryset = CarouselImageModel.objects.all()    context = {'images': queryset}    return render(request, "Encyclopedia/Home/HomeView.html", context)def register_view(request):    min_length = 8    error = 'Your Password is too short. Required Length is 8 Letters'    if request.method == 'POST':        form = UserForm(request.POST)        profile_form = ProfileForm(request.POST)        if form.is_valid() and profile_form.is_valid():            username = form.cleaned_data['username']            password = form.cleaned_data['password']            email = form.cleaned_data['email']            if len(password) < min_length:                return render(request, "Registration/register.html", {'form': form, 'error': error})            else:                User.objects.create_user(username, email, password)            return redirect('NBAE:home')    else:            form = UserForm()    return render(request, "Registration/register.html", {'form': form})def logout(request):    auth.logout(request)    return render(request, "Encyclopedia/Home/HomeView.html")def login(request):    if request.method == 'POST':        form = AuthenticationForm(request, request.POST)        if form.is_valid():            username = form.cleaned_data.get('username')            password = form.cleaned_data.get('password')            print(username, password)            user = auth.authenticate(username = username, password = password)            if user is not None:                auth.login(request, user)                messages.info(request, f"You are now logged in as {username}")                return redirect('/')            else:                messages.error(request, "Invalid username or password.")        else:            messages.error(request, "Invalid username or password.")    form = AuthenticationForm()    return render(request, "Registration/Login.html", {"form":form})def search_results(request):    query = request.GET.get('results')    list.append(query)    if query is not list[0] and query is not None:        list[0] = query    results = Records.objects.filter(Q(name__contains=list[0]) | Q(is_draft=True)).order_by('name')    paginator = Paginator(results, 1)    page = request.GET.get('page', 1)    try:        records = paginator.page(page)    except PageNotAnInteger:        records = paginator.page(1)    except EmptyPage:        records = paginator.page(paginator.num_pages)    context = {        'records': records,        'query' : query    }    return render(request, 'Encyclopedia/Record/search_results.html', context)def sort_view(request):    return render(request, 'Encyclopedia/Record/sort_by_records_list.html')def sort_by_records(request):    query = request.GET.get('choices')    list2.append(query)    if query is not list2[0] and query is not None:        list2[0] = query    if list2[0] == 'All':        results = Records.objects.all()    elif list2[0] == 'Player':        results = Records.objects.filter(type='Player')    elif list2[0] == 'Team':        results = Records.objects.filter(type='Team')    elif list2[0] == 'Season':        results = Records.objects.filter(type='Season')    elif list2[0] == 'Recently-Published':        results = Records.objects.all().order_by('published_date')    elif list2[0] == 'Verified':        results = Records.objects.filter(is_verified=True)    else:        results = Records.objects.all()    paginator = Paginator(results, 1)    page = request.GET.get('page', 1)    try:        records = paginator.page(page)    except PageNotAnInteger:        records = paginator.page(1)    except EmptyPage:        records = paginator.page(paginator.num_pages)    context = {        'records': records,        'query': query    }    return render(request, "Encyclopedia/Record/sort_by_records_list.html", context)@login_requireddef profile_view(request):    return render(request, "NBAE/profile_detail.html")@login_requireddef edit_profile(request):    if request.method == 'POST':        profile_form = UpdateProfileForm(request.POST,  request.FILES, instance=request.user.userprofile)        profile_form.instance.author = request.user        if request.FILES['image'] is not None:            profile_form.instance.image = request.FILES['image']        if profile_form.is_valid():            profile_form.save()            return redirect('NBAE:profile_view')    else:        profile_form = ProfileForm(instance=request.user.userprofile)    return render(request, "NBAE/profile_form.html", {'profile_form': profile_form})@login_requireddef create_view(request):    return render(request, "Encyclopedia/Record/Create.html")@login_requireddef playerconfirm_deleteview(request, pk):    player = get_object_or_404(PlayerRecords, pk=pk)    player_name = player.name    return render(request, "NBAE/playerrecords_confirm_delete.html", {'pk': pk, 'player': player_name})@login_requireddef teamconfirm_deleteview(request, pk):    team = get_object_or_404(TeamRecords, pk=pk)    team_name = team.name    return render(request, "NBAE/teamrecords_confirm_delete.html", {'pk': pk, 'team': team_name})@login_requireddef seasonconfirm_deleteview(request, pk):    season = get_object_or_404(SeasonRecords, pk=pk)    season_name = season.name    return render(request, "NBAE/seasonrecords_confirm_delete.html", {'pk': pk, 'season': season_name})@login_requireddef delete_playerrecord(request, pk):    global id    id += 1    record_to_delete = get_object_or_404(PlayerRecords, pk=pk)    delpost = DeletedRecord(id, record_to_delete.pk)    delpost.save()    record_to_delete.delete()    return redirect('NBAE:record_draft_list')@login_requireddef delete_seasonrecord(request, pk):    global id    id += 1    record_to_delete = get_object_or_404(SeasonRecords, pk=pk)    delpost = DeletedRecord(id, record_to_delete.pk)    delpost.save()    record_to_delete.delete()    return redirect('NBAE:record_draft_list')@login_requireddef delete_teamrecord(request, pk):    global id    id += 1    record_to_delete = get_object_or_404(TeamRecords, pk=pk)    delpost = DeletedRecord(id, record_to_delete.pk)    delpost.save()    record_to_delete.delete()    return redirect('NBAE:record_draft_list')@login_requireddef playerrecord_publish(request, pk):    record = get_object_or_404(PlayerRecords, pk=pk)    record.is_draft = False    record.publish()    return redirect('NBAE:playerrecord_detail', pk=pk)@login_requireddef teamrecord_publish(request, pk):    record = get_object_or_404(TeamRecords, pk=pk)    record.is_draft = False    record.publish()    return redirect('NBAE:teamrecord_detail', pk=pk)@login_requireddef seasonrecord_publish(request, pk):    record = get_object_or_404(SeasonRecords, pk=pk)    record.is_draft = False    record.publish()    return redirect('NBAE:seasonrecord_detail', pk=pk)@login_requireddef show_deleted_posts(request):    itemList = list()    objs = DeletedRecord.objects.all()    for i in objs:        itemList.append(i.post)    return render(request, "NBAE:deletedrecords", {'itemList': itemList})@login_requireddef add_comment_to_record(request, pk):    record = get_object_or_404(Records, pk=pk)    if request.method == "POST":        form = CommentForm(request.POST)        if form.is_valid():            comment = form.save(commit=False)            comment.record = record            comment.author = request.user            comment.save()            comment.approve()            if record.type == 'Player':                return redirect('NBAE:playerrecord_detail', pk=record.pk)            if record.type == 'Team':                return redirect('NBAE:teamrecord_detail', pk=record.pk)            if record.type == 'Season':                return redirect('NBAE:seasonrecord_detail', pk=record.pk)    else:        form = CommentForm()    return render(request, 'NBAE/comment_form.html', {'form': form})@login_requireddef comment_remove(request, pk):    comment = get_object_or_404(Comment, pk=pk)    record_pk = comment.record.pk    comment.delete()    if comment.record.type == 'Player':        return redirect('NBAE:playerrecord_detail', pk=record_pk)    if comment.record.type == 'Team':        return redirect('NBAE:teamrecord_detail', pk=record_pk)    if comment.record.type == 'Season':        return redirect('NBAE:seasonrecord_detail', pk=record_pk)