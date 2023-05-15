from django.db import models

# Create your models here.


class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=100)
    address = models.TextField(default="Caior")
    nationality = models.CharField(
        default="Egyptian", blank=True, null=True, max_length=50)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
