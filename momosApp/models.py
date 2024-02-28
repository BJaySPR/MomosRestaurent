from django.db import models

# Create your models here.
class Get_in_touch(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.IntegerField()
    message = models.CharField(max_length = 200, default=None)


    def __str__(self):
        return self.name