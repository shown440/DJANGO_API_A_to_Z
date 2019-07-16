# To create/ manipulate Database using models
from django.db import models


# Create your models here.

#########################################################################################################
###     Employees Details (Table)     
######################################################################################################

class Employee(models.Model):
    #id  = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    job_designation = models.CharField(max_length=50)
    manager_id  = models.IntegerField(default=None)
    date_of_birth = models.DateField()
    salary  = models.IntegerField()
    commission_amount  = models.IntegerField(default=None)
    dept_no  = models.IntegerField()

    # department = models.ForeignKey(
    #     'Department.department_no',
    #     on_delete = models.CASCADE
    # )


    #REQUIRED_FIELDS = ['ename', 'job', 'date_of_birth', 'sal', 'deptno']

    def full_name(self):
        """ Used to get a Users full name. """

        return self.employee_name
    
    def job_details(self):
        """ Used to get a Users job details. """

        return self.job_designation

    def mgr_id(self):
        """ Used to get a Users full name. """

        return self.manager_id

    def birth_date(self):
        """ Used to get a Users full name. """

        return self.date_of_birth

    def sal_amount(self):
        """ Used to get a Users full name. """

        return self.salary

    def comm_amount(self):
        """ Used to get a Users full name. """

        return self.commission_amount

    def dept_number(self):
        """ Used to get a Users full name. """

        return self.dept_no

    def __str__(self):
        """  Django uses this when it neds to convert the object to a String. """

        return self.employee_name


#########################################################################################################
###     Department Details (Table)     
######################################################################################################

class Department(models.Model):
    department_no = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=50)
    location  = models.CharField(max_length=50)

    # department = models.ForeignKey(
    #     'Employee',
    #     on_delete = models.CASCADE
    # )


    #REQUIRED_FIELDS = ['ename', 'job', 'date_of_birth', 'sal', 'deptno']

    def dept_number(self):
        """ Used to get a department number. """

        return self.department_no
    
    def dept_name(self):
        """ Used to get a department name. """

        return self.department_name

    def dept_location(self):
        """ Used to get a department location. """

        return self.location

    def __str__(self):
        """  Django uses this when it neds to convert the object to a String. """

        return self.department_name