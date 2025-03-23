from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from .models import Staff, IndividualMember
from .forms import LoginForm, IndividualForm, CooperateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

# Individual Form   
class IndividualView(FormView):
    template_name = 'individual_member.html'
    form_class = IndividualForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data.get('first_name'))
            form.save()
        return HttpResponse("Form submitted sucessfully")
    
# Cooperate View
class CooperateView(FormView):
    template_name = 'corporate_member.html'
    form_class = CooperateForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data.get('first_name'))
        return HttpResponse("Form submitted sucessfully")


def cooperate_view(request):
    if request.method == 'POST':
        form = CooperateForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Form submitted sucessfully")
    return render(request, 'individual_member.html', {'form': form})
        
@login_required
def logoutview(request):
    logout(request)
    print("Logged user out successfully")
    return redirect(reverse_lazy('home'))

def check_ind(request, pk):
    individual_member = IndividualMember.objects.get(id=pk)
    return render(request, 'ind_database.html', {'member': individual_member})


   


