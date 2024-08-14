from django import forms
from contact.models import Message

class ReponseForm(forms.ModelForm):
    class Meta:
        model=Message
        fiels =['response']
        exclude=['created_at','created_at','email','is_read','Message']
        labels = {
            'message':'Message',
        }
        widgets ={
            'response':forms.Textarea(attrs={'class':'form-control','row':3}),
        }

