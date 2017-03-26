from django.contrib import admin

# Register your models here.
from .models import Company
from .models import User
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    readonly_fields=('company_id',)
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(User)

