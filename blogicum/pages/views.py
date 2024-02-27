from django.shortcuts import render

# Create your views here.


def about(request):
    template = 'about.html'
    return render(request, template)


def rules(request):
    template = 'rules.html'
    return render(request, template)