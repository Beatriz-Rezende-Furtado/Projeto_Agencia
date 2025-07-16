from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Maquiador
from .forms import MaquiadorForm

def lista_maquiadores(request):
    maquiadores = Maquiador.objects.all()
    return render(
        request, 
        'maquiadores/lista.html', 
        {'maquiadores': maquiadores}
    )

@login_required
def novo_Maquiador(request):
    if request.method == 'POST':
        form = MaquiadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maquiadores:sucesso')
    else:
        form = MaquiadorForm()
    return render(request,
                  'maquiadores/form.html', 
                  {'form': form, 'titulo': 'Adicionar Maquiador'}
                )

@login_required
def editar_Maquiador(request, pk):
    maquiador = get_object_or_404(Maquiador, pk=pk)
    if request.method == 'POST':
        form = MaquiadorForm(request.POST, request.FILES, instance=maquiador)
        if form.is_valid():
            form.save()
            return redirect('maquiadores:lista_maquiadores')
    else:
        form = MaquiadorForm(instance=maquiador)
    return render(request, 
                  'maquiadores/form.html', 
                  {'form': form, 'titulo': 'Editar Maquiador'}
                )

@login_required
def deletar_Maquiador(request, pk):
    maquiador = get_object_or_404(Maquiador, pk=pk)
    if request.method == 'POST':
        maquiador.delete()
        return redirect('maquiadores:lista_maquiadores')
    return render(
        request, 
        'maquiadores/delete.html', 
        {'maquiadores': maquiador}
    )

def sucesso(request):
    return render(request, 'estilistas/sucesso.html')