from django.http import HttpResponse
from os import path

test_pass =  path.isfile(r'static\app\content\success.txt')

def home(request):
    return HttpResponse('SUCCESS' if test_pass else 'FAILURE')
