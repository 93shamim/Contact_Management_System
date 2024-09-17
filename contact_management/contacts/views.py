from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


def contact_details(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/contact_details.html', {'contact': contact})


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect('home')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})

# def search_contacts(request):
#     query = request.GET.get('q')
#     contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
#     return render(request, 'contacts/home.html', {'contacts': contacts})


# For search -using Button
def search_contacts(request):
    query = request.GET.get('q', '')
    contacts = Contact.objects.filter(
        Q(first_name__icontains=query) | 
        Q(last_name__icontains=query) | 
        Q(email__icontains=query) |
        Q(phone_number__icontains=query) |
        Q(address__icontains=query)
    )
    return render(request, 'contacts/home.html', {'contacts': contacts})


# # For instant search
# def instant_search(request):
#     query = request.GET.get('q', '')
#     contacts = Contact.objects.filter(
#         Q(first_name__icontains=query) | 
#         Q(last_name__icontains=query) | 
#         Q(email__icontains=query)
#     )
    
#     results = [{'id': contact.id, 'name': f"{contact.first_name} {contact.last_name}", 'email': contact.email} for contact in contacts]
#     return JsonResponse(results, safe=False)