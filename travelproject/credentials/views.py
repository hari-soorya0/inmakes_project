from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        c_pass = request.POST['c_pass']

    # user = User.objects.create_user(username=username, password=password, firstname=firstname, lastname=lastname,
    #                                 email=email)
    # user.save()
    # print('User Created')
    return render(request, 'register.html')
