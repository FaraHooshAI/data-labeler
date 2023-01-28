from django.shortcuts import render
# farahoosh super user
def index(request):
    return render(request, 'mainapp/index.html')
