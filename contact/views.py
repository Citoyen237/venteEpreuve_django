from django.shortcuts import render, redirect
from .form import *
from .models import Message
from django.views.generic.edit import CreateView
from django.contrib import messages
# Create your views here.

def getcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès, une réponse vous serait envoyé pas email')
            return redirect('front.contact')  # Rediriger vers une page de remerciement ou autre
    else:
        form = ContactForm()
    context ={
        'form':form
    }
    return render(request, 'contact.html',context)

# class CreateContact(CreateView):
#    model = Message
#    form_class=ContactForm
#    template_name="contact.html"
#    success_url="/contact/"

#    def form_valid(self, form):
#       messages.success(self.request, 'Votre message a été envoyé avec succès, une réponse vous serait envoyé pas email')
#       return super().form_valid(form)