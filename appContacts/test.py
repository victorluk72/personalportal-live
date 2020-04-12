if request.method == 'POST':
    form_p = PersonalContactForm(request.POST, instance=p_contact)
    form_c = ChildFormset(request.POST, instance=p_contact)
    if form_p.is_valid() and form_c.is_valid():
        form_p.save()
        form_c.save()
        return redirect('/contacts/p_contacts')
