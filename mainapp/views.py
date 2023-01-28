from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, CreateView
from django.views import View
from .models import DataText, EmotionText
from .forms import DataRow
# farahoosh super user
def index(request):
    return render(request, 'mainapp/index.html')

class DataRowView(CreateView):
    model = DataText
    form_class = DataRow
    template_name = 'mainapp/data_row.html'
    success_url = reverse_lazy('nima')

class DataRowUpdateView(UpdateView):
    model = DataText
    form_class = DataRow
    template_name = 'mainapp/data_row.html'
    success_url = reverse_lazy('nima')    
   

