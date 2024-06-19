# encoder/forms.py
from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Enter your message')
    day_choice = forms.ChoiceField(
        choices=[('odd', 'Odd Day'), ('even', 'Even Day')],
        label='Select Day Type'
    )
