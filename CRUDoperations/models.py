from django.db import models

# Create your models here.


class customer(models.Model):
    Cust_id = models.IntegerField()
    Cust_name = models.CharField(max_length=100)
    Cust_type = models.CharField(max_length=30)

    def __str__(self):
        return self.Cust_name
