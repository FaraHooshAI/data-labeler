from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views import View
from .models import DataText, EmotionText
from .forms import DataRow
from django.db.models import F

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

    def get(self, request, *args, **kwargs):
        query = DataText.objects.filter(id = self.kwargs['pk'])
        return render(request, self.template_name,{
            'form': self.form_class(instance = query[0])
        })

    def post(self, request, *args, **kwargs):
        query = DataText.objects.filter(id = self.kwargs['pk'])[0]
        secondary_emotions = request.POST.getlist('emotion_secondary')

        for emotion in EmotionText.objects.filter(id__in = secondary_emotions):
            query.emotion_secondary.add(emotion)
            
        return render(request, self.template_name)