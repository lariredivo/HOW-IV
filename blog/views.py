from django.shortcuts import render, redirect
from blog.models import Assist
from blog.forms import AssistForm

def home(request):
    data = {}
    data['db'] = Assist.objects.all()
    return render(request, 'index.html', data)

def formulario(request):
    data = {}
    data['formulario'] = AssistForm()
    return render(request, 'formulario.html', data)

def create(request):
    formulario = AssistForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    data['formulario'] = AssistForm(instance=data['db'])
    return render(request, 'formulario.html', data)

def update(request, pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    formulario = AssistForm(request.POST or None, instance=data['db'])
    if formulario.is_valid():
        formulario.save()
        return redirect('home')

def delete(request, pk):
    db = Assist.objects.get(pk=pk)
    db.delete()
    return redirect('home')