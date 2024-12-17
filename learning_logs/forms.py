from django import forms
from .models import Topic, Entry

# Form for new topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'maxlength': 200,'style': 'height: 50px; width: 60%; font-family: cursive; border-radius: 10px; align-items: center; padding: 10px' })}

# Form for new entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs= {'placeholder': 'Enter the Entry here', 'cols': 80, 'style': 'border-radius: 10px; font-family: cursive; align-items: center; padding: 10px; width: 100%; height: fit-content'})}