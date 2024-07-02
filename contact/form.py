from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model=Message
        fiels =['email','Message']
        exclude=['created_at','created_at']
        labels = {
            'email':'Email',
            'message':'Message',
        }
        widgets ={
            'Message':forms.Textarea(attrs={'class':'form-control','row':3}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }