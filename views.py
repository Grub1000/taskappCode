from django.shortcuts import render
from django.contrib.auth.models import User
def taskAppHome(request):
    if User.is_authenticated:
        user = request.user.id
    context = {
        "user": user
    }
    return render(request, 'indexTodo.html', context)
def taskAppRegister(request):
    return render(request, 'taskAppFirstPage.html')