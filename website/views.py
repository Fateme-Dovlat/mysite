from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('<h1>This is test</h1>')

def json_test(request):
    return JsonResponse({'name':'fateme'})

# Create your views here.
