
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import CareerAdvice
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, QuestionForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from functools import reduce
from django.contrib import messages
from django.shortcuts import render, redirect   
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LogoutView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    
    
    
class CareerListView(LoginRequiredMixin, ListView):
    template_name = 'career.html'
    login_url = '/login/'
    model = CareerAdvice
    paginate_by = 2

    def get_queryset(self):
        tag = self.kwargs.get('param')
        return CareerAdvice.objects.filter(tags__name__iexact=tag)    
    
    
    
class CourseDetailView(DetailView):
    template_name = 'course-details.html'
    model=CareerAdvice
    form_class = QuestionForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'object': self.object})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form, 'object': self.object})

    

class RegformPageView(CreateView):
    template_name = 'regform.html'     
    form_class = RegistrationForm   
    success_url = reverse_lazy('scaapp:loginform')



def SearchView(request):
    query = request.GET.get("q")
    words = query.split()
    careers = CareerAdvice.objects.filter(
        reduce(lambda x, y: x | y, [Q(name__icontains=word) for word in words])).order_by('-name') 
    if not careers:
        print("no results")  
    paginator = Paginator(careers, 10)
    page = request.GET.get('page')
    careers = paginator.get_page(page)
    context={"careers": careers}
    
    return render(request, 'search.html', context)    