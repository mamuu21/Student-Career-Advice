from django.contrib.auth.forms import UserCreationForm
from .models import Student, Question
from django import forms
from .models import User



class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields



class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)    

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['email', 'text']
		
    