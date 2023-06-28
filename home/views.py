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
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
