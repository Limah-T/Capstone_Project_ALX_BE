from django.contrib import admin
from .models import CustomUser, Director, IndividualMember, CorporateMember, Staff

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'last_login']
    list_filter = ['username', 'email', 'is_active']
    search_fields = ['username', 'email']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phonenumber', 'position', 'gender', 'account_number']
    list_filter = ['position']
    search_fields = ['first_name', 'email', 'phonenumber']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phonenumber', 'position_in_chambers', 'gender', 'is_active']
    list_filter = ['position_in_chambers']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(IndividualMember)
class IndividualMemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phonenumber', 'profession', 'gender', 'sponsor']
    list_filter = ['profession']
    search_fields = ['first_name', 'last_name', 'email', 'phonenumber', 'profession']

@admin.register(CorporateMember)
class CorporateMemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phonenumber', 'company_name', 'position_in_company', 'gender', 'sponsor']
    list_filter = ['position_in_company', 'company_name']
    search_fields = ['first_name', 'last_name', 'company_name']



