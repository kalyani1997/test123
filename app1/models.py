from django.db import models

# Create your models here.
class Candidate(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobno=models.IntegerField()
    remark=models.CharField()
    class Meta:
        db_table='can_info'