from django.urls import path

from assignment.web.views import SignInView, EmployeesView, CreateEmployeeView, EmployeeUpdateView, DeleteEmployeeView, \
    SignOutView

# defining the urls
urlpatterns = (
    path('', SignInView.as_view(), name='index'),
    path('logged/', EmployeesView.as_view(), name='employees view'),
    path('add-employee/', CreateEmployeeView.as_view(), name='add employee'),
    path('edit-employee/<int:pk>', EmployeeUpdateView.as_view(), name='edit employee'),
    path('delete-employee/<int:pk>', DeleteEmployeeView.as_view(), name='delete employee'),
    path('sign-ou/', SignOutView.as_view(), name='sign out'),

)
