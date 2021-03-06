# To create/ manipulate Database using models
from django.db import models

##########################################################
###     FOR CUSTOM DJANGO ADMIN USER 
##########################################################
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# To manage UserProfileManager
from django.contrib.auth.models import BaseUserManager



# Create your models here.

#########################################################################################################
###     Create Custom Admin management (Table)
#########################################################################################################
class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model. """

    def create_user(self, email, first_name, last_name, password=None):
        """ Create a new user profile object """

        if not email:
            raise ValueError("User must have an email address.")

        #name = first_name+" "+last_name
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """ Creates and save a new Superuser/Administrative user with given details. """
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represent a "user profile" inside our system. """

    email = models.EmailField(max_length=255, unique=True)
    first_name  = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """ Used to get a Users full name. """

        return self.first_name
        #, self.last_name

    def get_short_name(self):
        """ Used to get a Users short name. """

        return self.first_name

    def __str__(self):
        """  Django uses this when it neds to convert the object to a String. """

        return self.email
        # here we have to return Unique value. Email is unique here



#########################################################################################################
###     Employees Details (Table)     
######################################################################################################

class Employee(models.Model):
    #id  = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    mgr  = models.IntegerField(default=None)
    date_of_birth = models.DateField()
    sal  = models.IntegerField()
    comm  = models.IntegerField(default=None)
    deptno  = models.IntegerField()


    #REQUIRED_FIELDS = ['ename', 'job', 'date_of_birth', 'sal', 'deptno']

    def full_name(self):
        """ Used to get a Users full name. """

        return self.ename
    
    def job_details(self):
        """ Used to get a Users job details. """

        return self.job

    def mgr_id(self):
        """ Used to get a Users full name. """

        return self.mgr

    def birth_date(self):
        """ Used to get a Users full name. """

        return self.date_of_birth

    def sal_amount(self):
        """ Used to get a Users full name. """

        return self.sal

    def comm_amount(self):
        """ Used to get a Users full name. """

        return self.comm

    def dept_number(self):
        """ Used to get a Users full name. """

        return self.deptno

    def __str__(self):
        """  Django uses this when it neds to convert the object to a String. """

        return self.ename