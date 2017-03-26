from django.contrib import admin

# Register your models here.
from .models import Company
from .models import User

admin.site.register(Company)
admin.site.register(User)
