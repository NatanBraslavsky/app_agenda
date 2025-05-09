from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).all().order_by('-id')[0:10]
    context = {
        'contacts' : contacts,
    }
    return render(request, 'contact/index.html',context)#direcionar a url do html

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id)
    
    context = {
        'contact' : single_contact,
    }
    return render(request, 'contact/contact.html',context)#direcionar a url do html

