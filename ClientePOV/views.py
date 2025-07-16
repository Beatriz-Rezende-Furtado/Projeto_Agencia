from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sejaModelo(request):
    return render(request, 'sejaModelo.html')

def Equipe(request):
    return render(request, 'Equipe.html')

def analisando(request):
    if request.method == 'POST':
        return render(request, 'analisando.html')
    return redirect('home') 
 