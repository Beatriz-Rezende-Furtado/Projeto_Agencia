from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fotografo
from .forms import FotografoForm

# Create your views here.
def lista_fotografos(request):
    fotografos = Fotografo.objects.all()
    return render(request, 'fotografos/lista.html', {'fotografos': fotografos})

@login_required
def novo_Fotografo(request):
    if request.method == 'POST':
        form = FotografoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fotografos:sucesso')
    else:
        form = FotografoForm()
    return render(
        request, 
        'fotografos/form.html', 
        {'form': form, 'titulo': 'Adicionar Fotografo'})

@login_required
def editar_Fotografo(request, pk):
    fotografo = get_object_or_404(Fotografo, pk=pk)
    if request.method == 'POST':
        form = FotografoForm(request.POST, request.FILES, instance=fotografo)
        if form.is_valid():
            form.save()
            return redirect('fotografos:lista_fotografos')
    else:
        form = FotografoForm(instance=fotografo)
    return render(
        request, 
        'fotografos/form.html', 
        {'form': form, 'titulo': 'Editar Fotografo'}
    )

@login_required
def deletar_Fotografo(request, pk):
    fotografo = get_object_or_404(Fotografo, pk=pk)
    if request.method == 'POST':
        fotografo.delete()
        return redirect('fotografos:lista_fotografos')
    return render(
        request, 
        'fotografos/delete.html', 
        {'fotografos': fotografo})
    
def sucesso(request):
    return render(request, 'fotografos/sucesso.html')



