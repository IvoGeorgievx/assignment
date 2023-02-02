from django.contrib.auth import get_user_model, views
from django.urls import reverse_lazy
from django.views import generic as extra_views

from assignment.web.forms import EmployeeDeleteForm
from assignment.web.models import Employees

UserModel = get_user_model()


class SignInView(views.LoginView):
    template_name = 'index.html'
    success_url = reverse_lazy('employees view')


class EmployeesView(extra_views.ListView):
    model = Employees
    template_name = 'logged.html'

    # Ordering the objects by first name
    def get_queryset(self):
        return Employees.objects.all().order_by('first_name')


class CreateEmployeeView(extra_views.CreateView):
    model = Employees
    fields = '__all__'
    template_name = 'add_employee.html'
    success_url = reverse_lazy('employees view')


class EmployeeUpdateView(extra_views.UpdateView):
    model = Employees
    fields = '__all__'
    template_name = 'edit_employee.html'
    success_url = reverse_lazy('employees view')


class DeleteEmployeeView(extra_views.DeleteView):
    template_name = 'delete_employee.html'
    model = Employees
    form_class = EmployeeDeleteForm
    success_url = reverse_lazy('employees view')


class SignOutView(views.LogoutView):
    template_name = 'sign-out.html'
