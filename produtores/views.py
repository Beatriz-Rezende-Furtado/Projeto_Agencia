from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produtor
from .forms import ProdutorForm

# Create your views here.
def lista_produtores(request):
    produtores = Produtor.objects.all()
    return render(
        request, 
        'produtores/lista.html', 
        {'produtores': produtores}
    )

@login_required
def novo_Produtor(request):
    if request.method == 'POST':
        form = ProdutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produtores:sucesso')
    else:
        form = ProdutorForm()
    return render(
        request, 
        'produtores/form.html', 
        {'form': form, 'titulo': 'Adicionar Produtor'}
    )

@login_required
def editar_Produtor(request, pk):
    produtor = get_object_or_404(Produtor, pk=pk)
    if request.method == 'POST':
        form = ProdutorForm(request.POST, request.FILES, instance=produtor)
        if form.is_valid():
            form.save()
            return redirect('produtores:lista_produtores')
    else:
        form = ProdutorForm(instance=produtor)
    return render(
        request, 
        'produtores/form.html',
        {'form': form, 'titulo': 'Editar Produtor'}
    )

@login_required
def deletar_Produtor(request, pk):
    produtor = get_object_or_404(Produtor, pk=pk)
    if request.method == 'POST':
        produtor.delete()
        return redirect('produtores:lista_produtores')
    return render(
        request, 
        'produtores/delete.html', 
        {'produtores': produtor}
    )
    
def sucesso(request):
    return render(request, 'produtores/sucesso.html')
