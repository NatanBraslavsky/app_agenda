from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact



def index(request):
    contacts = Contact.objects.filter(show=True).all().order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'title' : 'Contatos - '
    }
    return render(request, 'contact/index.html',context)#direcionar a url do html

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(id__icontains=search_value) |
    Q(last_name__icontains=search_value) | Q(phone__icontains=search_value) | Q(email__icontains=search_value)).order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'title' : 'Search - '
    }
    return render(request, 'contact/index.html',context)#direcionar a url do html


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    title_contact = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact' : single_contact,
        'title' : title_contact
    }
    return render(request, 'contact/contact.html',context)#direcionar a url do html

