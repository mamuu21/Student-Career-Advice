from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", null=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
   
class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class Question(models.Model):
    text = models.TextField()
    student = models.ManyToManyField(Student, through='Student_Question', related_name='questions')
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.text[:50]


class Student_Question(models.Model):
    studdent = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.studdent.name



class CareerAdvice(models.Model):
    advisor = models.ManyToManyField(Advisor, through='Advisor_Advice', related_name='advice')
    name = models.CharField(max_length=255, null=True)
    content = models.TextField()
    content1 = models.TextField(null=True)
    content2 = models.TextField(null=True)
    content3 = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True)
    tags = TaggableManager()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("scaapp:course-detail", kwargs={"pk": self.pk})
    


class Advisor_Advice(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    advice = models.ForeignKey(CareerAdvice, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.question[:10]
        

    
 
    

    
    