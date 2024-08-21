from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EmsysUserManager(BaseUserManager):
    def create_user(self, username, name, department, student_number, gender, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not name:
            raise ValueError('The Name field must be set')
        if not department:
            raise ValueError('The Department field must be set')
        if not student_number:
            raise ValueError('The Student Number field must be set')
        if not gender:
            raise ValueError('The Gender field must be set')

        user = self.model(
            username=username,
            name=name,
            department=department,
            student_number=student_number,
            gender=gender,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, department, student_number, gender, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            username=username,
            name=name,
            department=department,
            student_number=student_number,
            gender=gender,
            password=password,
            **extra_fields
        )

class EmsysUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    student_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'department', 'student_number', 'gender']

    objects = EmsysUserManager()

    def __str__(self):
        return f'{self.username} / 이름 : {self.name} / 학번 : {self.student_number}'
