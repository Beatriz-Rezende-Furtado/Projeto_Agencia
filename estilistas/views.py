from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Estilista
from .forms import EstilistaForm

# Create your views here.
def lista_estilistas(request):
    estilistas = Estilista.objects.all()
    return render(
        request, 
        'estilistas/lista.html', 
        {'estilistas': estilistas}
    )

@login_required
def novo_Estilista(request):
    if request.method == 'POST':
        form = EstilistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('estilistas:sucesso')
    else:
        form = EstilistaForm()
    return render(
        request,
        'estilistas/form.html', 
        {'form': form, 'titulo': 'Adicionar Estilista'}
    )

@login_required
def editar_Estilista(request, pk):
    estilista = get_object_or_404(Estilista, pk=pk)
    if request.method == 'POST':
        form = EstilistaForm(request.POST, request.FILES, instance=estilista)
        if form.is_valid():
            form.save()
            return redirect('estilistas:lista_estilistas')
    else:
        form = EstilistaForm(instance=estilista)
    return render(
        request, 
        'estilistas/form.html', 
        {'form': form, 'titulo': 'Editar Estilista'}
    )

@login_required
def deletar_Estilista(request, pk):
    estilista = get_object_or_404(Estilista, pk=pk)
    if request.method == 'POST':
        estilista.delete()
        return redirect('estilistas:lista_estilistas')
    return render(
        request,
        'estilistas/delete.html',
        {'estilistas': estilista}
    )
    
def sucesso(request):
    return render(request, 'estilistas/sucesso.html')

