from django.db import models

# Create your models here.
class Company (models.Model):
	company_id = models.AutoField(primary_key=True)
	company_name = models.TextField()

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.TextField()
	company_id = models.ForeignKey(Company)
