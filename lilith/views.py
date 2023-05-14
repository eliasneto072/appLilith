from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Comentario
from .forms import ComentarioForm

@login_required
def homeView(request):
    context={}
    return render(request, 'home.html', context)

def create(request):
    form = ComentarioForm()
    context={'form':form}
    return render(request, 'form.html', context)

def createView(request):
    context={}
    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar') 
        
def listarView(request):
    user = Comentario.objects.order_by('-create')
    context={'user':user,}
    return render(request, 'listar.html', context)
    

def updateView(request,id):
    user = Comentario.objects.get(id=id)
    form = ComentarioForm(instance=user)
    if request.method == 'POST':
        form = ComentarioForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        context={'user':user, 'form':form }
        return render(request, 'editar.html', context)

def deleteView(request, id):
    comentario = Comentario.objects.get(id=id)
    form = ComentarioForm(instance=comentario)
    if request.method == 'POST':
        comentario.delete()
        return redirect('listar')
    else:
        context={'comentario':comentario, 'form':form}
        return render(request, 'delete.html', context)






