from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
	return JsonResponse({"Estado":1}) #Funciona