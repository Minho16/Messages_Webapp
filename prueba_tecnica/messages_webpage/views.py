from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Message
from .forms import MessageSaveForm
from django.utils import timezone


def home(request):
    messages = Message.objects.all().order_by("-time")[0:10]
    return render(request, 'messages_webpage/home.html', {
        'messages': messages,
    })


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            name = request.POST['username']
            Message.objects.create(userid_id=request.user.id, username=name,
                                   text="Hi, I am new here!", time=timezone.now())
        return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'messages_webpage/register.html', {'form': form})


def notfound(request):
    return render(request, 'messages_webpage/notfound.html')


def user_page(request, name):
    usermessages = Message.objects.all().filter(username=(name)).order_by("-time")

    if len(usermessages) == 0:
        return redirect('notfound')
    else:
        if request.method == "POST":
            form = MessageSaveForm(request.POST)
            texto = request.POST['text']

            # Better if MessageSaveForm works, not having to save the message manually
            Message.objects.create(
                userid_id=request.user.id, username=name, text=texto, time=timezone.now())

            if form.is_valid():
                return redirect('home')
            else:
                print(form.errors)
        else:
            form = MessageSaveForm()

        return render(request, 'messages_webpage/user_page.html', {
            'messages': usermessages,
            'message_name': usermessages[0].username,
            'form': form,
        })
