from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .forms import UserForm


def index(request):
    submitbutton = request.POST.get("submit")

    username = ''
    firstname = ''
    lastname = ''
    emailvalue = ''

    users = User.objects.all()
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        firstname = form.cleaned_data.get("first_name")
        lastname = form.cleaned_data.get("last_name")
        emailvalue = form.cleaned_data.get("email")
        for i in users:
            if i.username == username:
                return JsonResponse({'Status': 403,
                                     'Content-Type': 'application/json',
                                     'Body':
                                         {
                                             'message': 'Login failed'
                                         }
                                     })
            else:
                user = User.objects.create_user(username)
                user.first_name = firstname
                user.last_name = lastname
                user.email = emailvalue
                user.save()

    return render(request, 'catalog/index.html', {'form': form})


def auth(request):
    user = User.objects.create_user(username, user_email, user_password, user_first_name, user_last_name)
    user.save()
    return HttpResponse('Пользователь создан')
