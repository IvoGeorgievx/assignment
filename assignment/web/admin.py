from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from assignment.web.models import Employees

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'last_login', 'is_superuser', 'is_staff']
    list_filter = ()


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    pass
