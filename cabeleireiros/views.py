from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cabeleireiro
from .forms import CabeleireiroForm


# Create your views here.
def lista_cabeleireiros(request):
    cabeleireiros = Cabeleireiro.objects.all()
    return render(
        request, 
        'cabeleireiros/lista.html', 
        {'cabeleireiros': cabeleireiros}
    )

@login_required
def novo_Cabeleireiro(request):
    if request.method == 'POST':
        form = CabeleireiroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cabeleireiros:sucesso')
    else:
        form = CabeleireiroForm()
    return render(
        request, 
        'cabeleireiros/form.html', 
        {'form': form, 'titulo': 'Adicionar Cabeleireiro'}
    )

@login_required
def editar_Cabeleireiro(request, pk):
    cabeleireiro = get_object_or_404(Cabeleireiro, pk=pk)
    if request.method == 'POST':
        form = CabeleireiroForm(request.POST, request.FILES, instance=cabeleireiro)
        if form.is_valid():
            form.save()
            return redirect('cabeleireiros:lista_cabeleireiros')
    else:
        form = CabeleireiroForm(instance=cabeleireiro)
    return render(
        request, 
        'cabeleireiros/form.html',
        {'form': form, 'titulo': 'Editar Cabeleireiro'}
    )

@login_required
def deletar_Cabeleireiro(request, pk):
    cabeleireiro = get_object_or_404(Cabeleireiro, pk=pk)
    if request.method == 'POST':
        cabeleireiro.delete()
        return redirect('cabeleireiros:lista_cabeleireiros')
    return render(
        request, 
        'cabeleireiros/delete.html', 
        {'cabeleireiro': cabeleireiro})

def sucesso(request):
    return render(request, 'cabeleireiros/sucesso.html')

