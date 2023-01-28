from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views import View
from .models import DataText, EmotionText
from .forms import DataRow
# farahoosh super user
def index(request):
    return render(request, 'mainapp/index.html')

class DataRow(CreateView):
    model = DataText
    form_class = DataRow
    template_name = 'mainapp/data_row.html'
    success_url = 'mainapp/index.html'
    print([x for x in EmotionText.objects.all()])
   

