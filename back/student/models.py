from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class ClassName(models.Model) :
  name = models.CharField("반이름", max_length=5)
  
  def __str__(self) :
    return self.name


class Student(models.Model) : 
  name = models.CharField("이름", max_length=100)
  class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
  
  def __str__(self) :
    return f'{self.class_name.name, self.name}'
  
