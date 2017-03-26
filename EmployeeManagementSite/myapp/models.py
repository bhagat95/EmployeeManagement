from django.db import models

# Create your models here.
class Company (models.Model):
	company_id = models.AutoField(primary_key=True)
	company_name = models.TextField()
	
	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.company_id

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.TextField()
	company_id = models.ForeignKey(Company)
	
	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.user_id
