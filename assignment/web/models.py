from django.db import models
from django.contrib.auth import models as auth_models

from assignment.web.managers import AppUserManager
from assignment.web.validators import validate_length, validate_name_length


# Extending the default Django user so I can login with email. (Permissions mixin to add users permissions)
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True,
                              null=False,
                              blank=False, )

    is_staff = models.BooleanField(default=False,
                                   null=False,
                                   blank=False, )
    # This indicates that the user will Log in with email
    USERNAME_FIELD = 'email'
    objects = AppUserManager()


# Creating Employee model in the database
class Employees(models.Model):
    class Meta:
        # displaying the proper name in the admin panel
        verbose_name_plural = 'Employees'

    choices = (
        ("Engineering", "Engineering"),
        ("HR", "HR"),
        ("Finance", "Finance"),

    )

    first_name = models.CharField(max_length=254,
                                  null=False,
                                  blank=False,
                                  validators=[validate_name_length])

    last_name = models.CharField(max_length=254,
                                 null=False,
                                 blank=False,
                                 validators=[validate_name_length])

    address = models.CharField(max_length=254,
                               null=True,
                               blank=True)

    phone = models.CharField(null=False,
                             blank=False,
                             unique=True,
                             validators=[validate_length],
                             max_length=254)

    department = models.CharField(max_length=50,
                                  choices=choices,
                                  null=False,
                                  blank=False)

    position = models.CharField(max_length=254,
                                null=False,
                                blank=False)

    salary = models.IntegerField(null=False,
                                 blank=False)

    # changes the way that employees are shown in the admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
