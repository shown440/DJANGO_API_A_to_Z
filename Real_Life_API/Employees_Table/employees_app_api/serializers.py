from rest_framework import serializers

from . import models


#########################################################################################################
###     Serializer for Employees Details (Table) 
#########################################################################################################

class EmployeeSerializer(serializers.ModelSerializer):
    """ serializers.ModelSerializer imported from django rest_framework. """
    """ A serializer for our Employee objects to make it JSON data. """

    class Meta:
        model = models.Employee
        fields = ('id', 'employee_name', 'job_designation', 'manager_id', 'date_of_birth', 'salary', 'commission_amount', 'dept_no')

    def create(self, validated_data):
        """ Create and return a new User. """

        user = models.Employee(
            employee_name = validated_data['employee_name'],
            job_designation = validated_data['job_designation'],
            manager_id = validated_data['manager_id'],
            date_of_birth = validated_data['date_of_birth'],
            salary = validated_data['salary'],
            commission_amount = validated_data['commission_amount'],
            dept_no = validated_data['dept_no']

        )

        user.save()

        return user


#########################################################################################################
###     Serializer for Department Details (Table) 
#########################################################################################################

class DepartmentSerializer(serializers.ModelSerializer):
    """ serializers.ModelSerializer imported from django rest_framework. """
    """ A serializer for our Department objects to make it JSON data. """

    class Meta:
        model = models.Department
        fields = ('department_no', 'department_name', 'location')

    def create(self, validated_data):
        """ Create and return a new User. """

        department = models.Department(
            department_no = validated_data['department_no'],
            department_name = validated_data['department_name'],
            location = validated_data['location'],
        )

        department.save()

        return department