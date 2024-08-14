from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model=Message
        fiels =['email','Message','response']
        exclude=['created_at','created_at','is_read']
        labels = {
            'email':'Email',
            'message':'Message',
            'response':'response',
        }
        widgets ={
            'response':forms.Textarea(attrs={'class':'form-control','row':3}),
            'Message':forms.Textarea(attrs={'class':'form-control','row':3}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }