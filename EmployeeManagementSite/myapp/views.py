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

def add_company(request, company_name):
	resp = 'success'
	q = Company(company_name=company_name)
	q.save()
	return HttpResponse(json.dumps(resp), content_type="application/json")

def delete_company(request, company_id):
	resp = "success"
	User.objects.filter(company_id__company_id=company_id).delete()
	Company.objects.filter(company_id=company_id)
	return HttpResponse(json.dumps(resp), content_type="application/json")
	
def add_user(request, user_name, company_id):
	resp = "success"
	q = User(user_name=user_name, company_id__company_id=company_id)
	q.save()
	return HttpResponse(json.dumps(resp), content_type="application/json")
	
def fetch(request):
	dic = {}
	dic['User'] = []
	for i in User.objects.all():
		dic['User'].append(i.user_name)
	return HttpResponse(json.dumps(dic), content_type="application/json")
