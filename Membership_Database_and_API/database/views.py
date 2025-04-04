from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Staff, IndividualMember, CorporateMember, Director, CustomUser
from .forms import LoginForm, IndividualForm, CorporateForm

def custom_404_page(request, exception):
    return render(request, '404.html', status=400)

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
            user = authenticate(self.request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(self.request, 'Logged In')   
                return super().post(request, *args, **kwargs)          
            messages.error(self.request, 'Email or Password is Incorrect!')
        messages.error(self.request, "Invalid email address")
        return redirect(reverse_lazy('login_view'))

# Individual Form View (CBV)
class IndividualView(FormView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = "database.change_individualmember"
    permission_denied_message = "You do not have permission to view the form page!"
    template_name = 'individual_member.html'
    form_class = IndividualForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            current_user = get_object_or_404(CustomUser, id=request.user.id)
            member = form.save(commit=False)
            member.creator_id = current_user.id
            member.save()
            return render(request, 'form_submission.html', {'member': member, 'creator': current_user.username.title()})
        return super().post(request, *args, **kwargs)
    
# Corporate Form View(CBV)
class CorporateView(FormView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = "database.change_corporatemember"
    permission_denied_message = "You do not have permission to view the form page!"
    template_name = 'corporate_member.html'
    form_class = CorporateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            current_user = get_object_or_404(CustomUser, id=request.user.id)
            member = form.save(commit=False)
            member.creator_id = current_user.id
            member.save()
            return render(request, 'form_submission.html', {'member': member, 'creator': current_user.username.title()})
        return super().post(request, *args, **kwargs)
        
@login_required
def logoutview(request):
    logout(request)
    print("Logged user out successfully")
    return redirect(reverse_lazy('home'))

# Class Based view for individual list view
class IndividualDataBaseView(generic.ListView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = "database.view_individualmember"
    permission_denied_message = "You do not have permission to view the database!"
    model = IndividualMember
    template_name = 'ind_database.html'
    context_object_name = 'members'
    ordering = 'first_name'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
   
# Class Based view for individual detail view
class IndividualDetailView(generic.DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = "database.view_individualmember"
    permission_denied_message = "You do not have permission to view the database!"
    model = IndividualMember
    template_name = 'ind_detail_view.html'
    context_object_name = 'member'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
# Class Based view for corporate list view
class CorporateDatabaseView(generic.ListView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = "database.view_corporatemember"
    permission_denied_message = "You do not have permission to view the database!"
    model = CorporateMember
    template_name = 'cop_database.html'
    context_object_name = 'members'
    ordering = 'first_name'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)

# Class Based view for corporate detail view
class CorporateDetailView(generic.DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = "login_view"
    permission_required = "database.view_corporatemember"
    permission_denied_message = "You do not have permission to view the database!"
    model = CorporateMember
    template_name = 'cop_detail_view.html'
    context_object_name = 'member'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
# Class Based view for staff list view
class StaffDatabaseView(generic.ListView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = "database.view_staff"
    permission_denied_message = "You do not have permission to view the database!"
    model = Staff
    template_name = 'staff_database.html'
    context_object_name = 'all_staff'
    ordering = 'first_name'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)

# Class Based View for staff detail view
class StaffDetailView(generic.DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = "login_view"
    permission_required = "database.view_staff"
    permission_denied_message = "You do not have permission to view the database!"
    model = Staff
    template_name = 'staff_detail_view.html'
    context_object_name = 'staff'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)

# Class Based View for director list view
class DirectorDatabaseView(generic.ListView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'login_view'
    permission_required = 'database.view_director'
    permission_denied_message = 'You do not have permission to view the database!'
    model = Director
    template_name = 'bod_database.html'
    context_object_name = 'directors'
    ordering = 'first_name'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)

# Class Based View for director detail view
class DirectorDetailView(generic.DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login_view'
    permission_required = 'database.view_director'
    permission_denied_message = 'You do not have permission to view the database!'
    model = Director
    template_name = 'bod_detail_view.html'
    context_object_name = 'director'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.redirect_field_name)
        if not request.user.has_perm(self.permission_required):
            messages.error(request, message=self.permission_denied_message)
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)