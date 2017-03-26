from django.shortcuts import render
from myapp.models import User, Company
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")

def fetch_users(request, company_id):
	dic = {}
	dic['User'] =[]
	print("fetched company id is"+company_id)
	u=User.objects.filter(company_id__company_id=company_id)
	for i in u:
		dic['User'].append(i.user_name)
	
	print(dic)
	return HttpResponse(json.dumps(dic), content_type="application/json")
	
