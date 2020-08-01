from django.shortcuts import render,HttpResponse,redirect,reverse
from message.models import Message
from django.contrib import messages



def index(request):
    return render(request, "index.html")


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def addMessage(request):

    if request.method == "POST":
        name = request.POST.get("txtName")
        email = request.POST.get("txtEmail")
        phone = request.POST.get("txtPhone")
        msg = request.POST.get("txtMsg")

        newMessage = Message(name_message = name, email_message = email, phone_message = phone, content_message = msg)

        newMessage.save()
    messages.success(request,"Mesajınız iletildi en kısa sürede iletişime geçilecektir")
    return redirect("index")
    

def test(request):
    return render(request,"test.html")