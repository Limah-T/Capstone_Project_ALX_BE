from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from .models import Staff, IndividualMember, CorporateMember, Director
from .forms import LoginForm, IndividualForm, CooperateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

def home(request):
    return render(request, 'home.html')

# LoginView 
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get("password")
            print(email, password)
            user = authenticate(self.request, email=email, password=password)
            if user:
                login(request, user)
                print("Logged user in successfully")
                messages.success(self.request, 'Logged In')   
                return super().post(request, *args, **kwargs)          
            messages.error(self.request, 'Email or Password is Incorrect!')
        messages.error(self.request, "Invalid email address")
        return redirect(reverse_lazy('login_view'))

# Individual Form View (CBV)
class IndividualView(FormView):
    template_name = 'individual_member.html'
    form_class = IndividualForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data.get('first_name'))
            form.save()
        return HttpResponse("Form submitted sucessfully")
    
# Cooperate Form View(CBV)
class CooperateView(FormView):
    template_name = 'corporate_member.html'
    form_class = CooperateForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data.get('first_name'))
        return HttpResponse("Form submitted sucessfully")
        
@login_required
def logoutview(request):
    logout(request)
    print("Logged user out successfully")
    return redirect(reverse_lazy('home'))

# Class Based view for individual list view
class IndividualDataBaseView(generic.ListView):
    model = IndividualMember
    template_name = 'ind_database.html'
    context_object_name = 'members'
    ordering = 'first_name'

# Class Based view for individual detail view
class IndividualDetailView(generic.DetailView):
    model = IndividualMember
    template_name = 'ind_detail_view.html'
    context_object_name = 'member'

# Class Based view for corporate list view
class CorporateDatabaseView(generic.ListView):
    model = CorporateMember
    template_name = 'cop_database.html'
    context_object_name = 'members'
    ordering = 'first_name'

# Class Based view for corporate detail view
class CorporateDetailView(generic.DetailView):
    model = CorporateMember
    template_name = 'cop_detail_view.html'
    context_object_name = 'member'
    
# Class Based view for staff list view
class StaffDatabaseView(generic.ListView):
    model = Staff
    template_name = 'staff_database.html'
    context_object_name = 'all_staff'
    ordering = 'first_name'

# Class Based View for staff detail view
class StaffDetailView(generic.DetailView):
    model = Staff
    template_name = 'staff_detail_view.html'
    context_object_name = 'staff'

# Class Based View for director list view
class DirectorDatabaseView(generic.ListView):
    model = Director
    template_name = 'bod_database.html'
    context_object_name = 'directors'

# Class Based View for director detail view
class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = 'bod_detail_view.html'
    context_object_name = 'director'