from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        "variable1": "This is sent variable 123",
        "variable2": "This is sent variable 456"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")


def about(request):
    return HttpResponse("This is about page")


def services(request):
    return HttpResponse("This is services page")


def contact(request):
    return HttpResponse("This is contact page")
