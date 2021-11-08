from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from clientes.models import Person
from .form import PersonForm

@login_required
def persorns_list(request):
    persons = Person.objects.all()

    context = {
        'persons': persons,
    }
    return render(request, 'people_list.html', context)

@login_required
def persorns_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('persorns_list')

    context = {
        'form': form,
    }
    return render(request, 'person_form.html', context)

@login_required
def persorns_update(request, id):
    person =get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None,
    instance=person)

    if form.is_valid():
        form.save()
        return redirect('persorns_list')

    context = {
        'form': form,
    }
    return render(request, 'peson_form.html', context)

@login_required
def persorns_delete(request, id):
    person =get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None,
    instance=person)

    context = {
        'form': form,
    }
    if request.method == 'POST':
        person.delete()
        return redirect('persorns_list')

    return render(request, 'persorns_delete_confirm.html', context)