from django.shortcuts import render, redirect, get_object_or_404
from .models import CEO
from .forms import CEOForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Big_Boss(request):
    ceo = CEO.objects.first()
    return render(
        request, 
        'CEO/boss.html',
        {'ceo': ceo}
    )

@login_required
def editar_ceo(request):
    ceo = CEO.objects.first()
    if not ceo:
        ceo = CEO.objects.create(nome='', bio='')

    if request.method == 'POST':
        form = CEOForm(request.POST, request.FILES, instance=ceo)
        if form.is_valid():
            form.save()
            return redirect('CEO:Big_Boss')
    else:
        form = CEOForm(instance=ceo)
    
    return render(
        request, 
        'CEO/form.html',
        {'form': form}
    )
