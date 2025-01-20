from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView



app_name = 'scaapp'
urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('career/<str:param>/', CareerListView.as_view(), name="career"),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name="course-detail"),
    path('regform/', RegformPageView.as_view(), name="regform"),
    path('login/', LoginView.as_view(template_name='loginform.html', next_page='scaapp:index'), name='loginform'),
    path('search/', SearchView, name='search'),
    path('logout/', LogoutView.as_view(template_name='logout.html', next_page='scaapp:index'), name='logout'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

