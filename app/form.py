from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        # fields='__all__'
        # fields=['topic_name','name']
        # labels={'topic_name':'TN'}
        exclude=['url']
        widgets={'email':forms.PasswordInput}

class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'

