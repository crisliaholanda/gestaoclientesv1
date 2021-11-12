from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from clientes.models import Person
from .form import PersonForm

@login_required
def persorns_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    '''
    para check box
    request.GET.get('check-box', None) > {str}'on'
    if check-box == 'on':
        persons.objects.filter(ativo=True)
    '''
  
    
    if nome or sobrenome:
        # persons = Person.objects.filter(first_name__icontains=nome, last_name__icontains=sobrenome)
        persons = Person.objects.filter(first_name__icontains=nome) | Person.objects.filter(last_name__icontains=sobrenome)
    else:
      persons = Person.objects.all()

    return render(request, 'people_list.html', {'persons': persons,})

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
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    
    if form.is_valid():
        form.save()
        return redirect('persorns_list')

    context = {
        'form': form,
    }
    print('aaaaaaaaaaa')
    return render(request, 'person_form.html', context)


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