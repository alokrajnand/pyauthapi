from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
# write the code of user manager


class MyUserManager(BaseUserManager):

    def create_user(self, phone_number, name, email_address, date_of_birth, password=None):
        if not phone_number:
            raise ValueError('Valid Phone Number is Required')

        if not email_address:
            raise ValueError('Valid Email Addreess is Required')

        if not name:
            raise ValueError('You Must have name')

        user_obj = self.model(
            phone_number=phone_number,
            name=name,
            email_address=self.normalize_email(email_address),
            date_of_birth=date_of_birth,

        )

        user_obj.set_password(password)
        user_obj.is_admin = False
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, phone_number, name,  email_address, date_of_birth, password=None):

        user_obj = self.create_user(
            phone_number,
            name,
            email_address,
            date_of_birth=date_of_birth,
            password=password,
        )
        user_obj.is_admin = True
        user_obj.save(using=self._db)
        return user_obj


# code for user model

class MyUser(AbstractBaseUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="phone number is not valid")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, unique=True)
    name = models.CharField(max_length=50, unique=False, blank=False)
    email_address = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['date_of_birth', 'email_address', 'name']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
