from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'catalog/form_register.html')



def register(request):
    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()
    return HttpResponse('Пользователь создан')