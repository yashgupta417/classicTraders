from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,username,password):
        """Creates and saves a User with the given username and password."""
        if not username:
            raise ValueError('User must have a username')
        if not password:
            raise ValueError('User must have a password')

        user=self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,username, password):
        """Creates and saves a staff user with the given email and password."""

        user = self.create_user(username=username,password=password)
        user.staff = True
        user.save(using=self._db)
        return user


    def create_superuser(self,username,password):
        """Creates and saves a superuser with the given username and password."""
        user = self.create_user(username,password=password)
        user.staff = True
        user.admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255,unique=True,blank=False,null=False)
    name=models.CharField(max_length=255,blank=True,null=True)
    role=models.CharField(max_length=20,blank=True,null=True)
    mobile_number=models.CharField(max_length=15,blank=True,null=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
    objects=UserManager()

    def __str__(self):
        return self.username
    

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `api`?"""
        return True

