from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Modelo
from .forms import ModeloForm



def lista_modelos(request):
    modelos = Modelo.objects.all()                    
    return render(
        request,
        'modelos/lista.html',
        {'modelos': modelos}
    )


@login_required
def novo_Modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('modelos:sucesso')  
    else:
        form = ModeloForm()
    return render(
        request,
        'modelos/form.html',
        {'form': form, 'titulo': 'Adicionar Modelo'}
    )


@login_required
def editar_Modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('modelos:lista_modelos')
    else:
        form = ModeloForm(instance=modelo)
    return render(
        request,
        'modelos/form.html',
        {'form': form, 'titulo': 'Editar Modelo'}
    )


@login_required
def deletar_Modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('modelos:lista_modelos')
    return render(
        request,
        'modelos/delete.html',
        {'modelo': modelo}
    )

def sucesso(request):
    return render(request, 'modelos/sucesso.html')