from django.shortcuts import render, redirect
from django.contrib import messages
# This to bring dictionaries from chices.py file
from appContacts.models import PersonalContact, ChildContact, BusinessContact, BusinesType
from appContacts.forms import BusinessContactForm, PersonalContactForm, ChildForm
from django.contrib.auth.decorators import login_required
from .filters import PContactFilter, BContactFilter, BAdvContactFilter, PAdvContactFilter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.forms import inlineformset_factory


# View function for p_contacts.html page
@login_required(login_url='login')
def func_p_contacts(request):

    personal_contacts = PersonalContact.objects.all()

    # Filtering logic here
    myPersonalFilter = PContactFilter(request.GET, queryset=personal_contacts)
    personal_contacts = myPersonalFilter.qs

    myAdvPersonalFilter = PAdvContactFilter(
        request.GET, queryset=personal_contacts)
    personal_contacts = myAdvPersonalFilter.qs

    # Paginator logic here
    paginator = Paginator(personal_contacts, 4)
    page = request.GET.get('page')
    paged_personal_contacts = paginator.get_page(page)

    args = {
        'personal_contacts': paged_personal_contacts,
        'myPersonalFilter': myPersonalFilter,
        'myAdvPersonalFilter': myAdvPersonalFilter
    }
    return render(request, 'contacts/p_contacts.html', args)

# View function for b_contacts.html page
@login_required(login_url='login')
def func_b_contacts(request):

    business_contacts = BusinessContact.objects.all()
    business_types = BusinesType.objects.all().order_by('name')

    # Filtering logic here
    myBusinessFilter = BContactFilter(request.GET, queryset=business_contacts)
    business_contacts = myBusinessFilter.qs

    myAdvBusinessFilter = BAdvContactFilter(
        request.GET, queryset=business_contacts)
    business_contacts = myAdvBusinessFilter.qs

    # Paginator logic here
    paginator = Paginator(business_contacts, 4)
    page = request.GET.get('page')
    paged_business_contacts = paginator.get_page(page)

    args = {
        'business_contacts': paged_business_contacts,
        'business_types': business_types,
        'myBusinessFilter': myBusinessFilter,
        'myAdvBusinessFilter': myAdvBusinessFilter
    }
    return render(request, 'contacts/b_contacts.html', args)

# ----Add personal contact---------------
@login_required(login_url='login')
def add_p_contact(request):
    form_p = PersonalContactForm()
    if request.method == 'POST':
        form_p = PersonalContactForm(request.POST)
        if form_p.is_valid():
            form_p.save()
            return redirect('/contacts/p_contacts')

    args = {'form_p': form_p}
    return render(request, 'contacts/personal_update1.html', args)

# ----Add business contact 1---------------
@login_required(login_url='login')
def add_b_contact(request):
    form_b = BusinessContactForm()
    if request.method == 'POST':
        form_b = BusinessContactForm(request.POST)
        if form_b.is_valid():
            form_b.save()
            return redirect('/contacts/b_contacts')

    args = {'form_b': form_b}
    return render(request, 'contacts/business_update1.html', args)


# ----Update personal contact---------------
@login_required(login_url='login')
#https://stackoverflow.com/questions/18489393/django-submit-two-different-forms-with-one-submit-button
def update_p_contact(request, pk_p_contact_id):
    p_contact = PersonalContact.objects.get(id=pk_p_contact_id)
    form_p = PersonalContactForm(instance=p_contact)

    ChildFormset = inlineformset_factory(PersonalContact, ChildContact, fields=(
        'firstName', 'lastName', 'birthday',), can_delete=False, extra=1)
    form_c = ChildFormset(instance=p_contact)

    if request.method == 'POST':
        form_p = PersonalContactForm(request.POST, instance=p_contact)
        form_c = ChildFormset(request.POST, instance=p_contact) #, prefix = 'form_c')
        if form_p.is_valid() and form_c.is_valid():
            form_p.save()
            form_c.save()
            print('valid p_form')
            return redirect('/contacts/p_contacts')
        else:
            print('invalid p_form')
            #print(form_p)

        # if form_c.is_valid():
        #     form_c.save()
        #     print('valid c_form')
        #     return redirect('/contacts/p_contacts')
        # else:
        #     print('invalid c_form')
        #     #print(form_c)    

    args = {'form_p': form_p,
            'form_c': form_c}
    return render(request, 'contacts/personal_update1.html', args)


# ----Update business contact 1---------------
@login_required(login_url='login')
def update_b_contact(request, pk_b_contact_id):
    b_contact = BusinessContact.objects.get(id=pk_b_contact_id)
    form_b = BusinessContactForm(instance=b_contact)

    if request.method == 'POST':
        form_b = BusinessContactForm(request.POST, instance=b_contact)
        if form_b.is_valid():
            form_b.save()
            return redirect('/contacts/b_contacts')

    args = {'form_b': form_b}
    return render(request, 'contacts/business_update1.html', args)


# ----Update business contact---------------
# @login_required(login_url='login')
# def update_b_contact(request, pk_b_contact_id):

#     b_contact = BusinessContact.objects.get(id=pk_b_contact_id)
#     business_types = BusinesType.objects.all().order_by('name')

#     if request.method == 'POST':
#         sameid = request.POST['id']
#         print()

#     args = {'b_contact': b_contact,
#             'business_types': business_types,
#             'state_choices': state_choices,
#             'country_choices': country_choices
#             }
#     return render(request, 'contacts/business_update.html', args)


# ----Delete personal contact---------------
@login_required(login_url='login')
def delete_p_contact(request, pk_p_contact_id):

    p_contact = PersonalContact.objects.get(id=pk_p_contact_id)
    if request.method == "POST":
        p_contact.delete()
        return redirect('/contacts/p_contacts')

    args = {'p_contact': p_contact}
    return render(request, 'contacts/p_delete.html', args)


# ----Delete business contact---------------
# @login_required(login_url='login')
def delete_b_contact(request, pk_b_contact_id):

    b_contact = BusinessContact.objects.get(id=pk_b_contact_id)
    if request.method == "POST":
        b_contact.delete()
        return redirect('/contacts/b_contacts')

    args = {'b_contact': b_contact}
    return render(request, 'contacts/b_delete.html', args)


# ----Add new business type to db---------------
@login_required(login_url='login')
def add_business_type(request):
    form_b = BusinessContactForm()
    args = {'form_b': form_b}
    if request.method == 'POST':
        # 1) Capture the field from form
        new_businessType = request.POST['businessType']

        # 2) check if business type exsist
        has_business_type = BusinesType.objects.all().filter(name=new_businessType)

        if has_business_type:
            messages.error(request, 'Thisi busness type already exist')
            return render(request, 'contacts/business_update1.html', args)
        else:
            business_type = BusinesType(name=new_businessType)
            # Save to database
            business_type.save()
            return render(request, 'contacts/business_update1.html', args)