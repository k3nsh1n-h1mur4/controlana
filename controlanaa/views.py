from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect, reverse
from django.core.paginator import Paginator

from django.contrib.auth.models import User 
from django.contrib.auth import login, logout

from .models import controlModel
from .forms import controlForm, controlFormm, createUserForm



def index(request):
    return HttpResponse('Index')

def login(request):
    title = 'Login'
    pass

def register_user(request):
    title = 'Registro Usuario'
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        if user:
            login(request, user)
            return redirect('login')
    else:
        form = createUserForm()
    return render(request, 'registration/create_user.html', {'form': form, 'title': title})


def register_new(request):
    title = 'Registro Nuevo'
    form = controlFormm()
    if request.method == 'POST':
        form = controlFormm(request.POST)
        ppta = request.POST['ppta']
        fecha = request.POST['fecha']
        aspirante = request.POST['aspirante']
        categoria = request.POST['categoria']
        propone = request.POST['propone']
        telefono = request.POST['telefono']
        zona = request.POST['zona']
        if form.is_valid():
            form.save(commit=True)       
            return redirect('list')
    else:
        form = controlFormm()

    return render(request, 'registro_nuevo.html', {'title': title, 'form': form})


def list(request):
    title = 'Listado General'
    if request.method == 'GET':
        ctx = controlModel.objects.all()
        paginator = Paginator(ctx, 12)
        print(paginator)

        page_number = request.GET.get("page")
        print(page_number)
        page_obj = paginator.get_page(page_number)
        for i in page_obj:
            print(i.ppta, i.fecha)
        #return render(request, 'listado.html', {'page_bj': page_obj, 'title': title})
    return render(request, "listado.html", {'page_obj': page_obj, 'ctx': ctx, 'title': title})
    """
    if request.method == 'GET':
        ctx = controlModel.objects.all()
        if ctx is None:
            return HttpResponse('Sin datos que mostrar')
        else:
            return render(request, 'listado.html', {'ctx': ctx})
    return render(request, 'listado.html', {'ctx': ctx, 'title': title})
    """

def editar(request, id):
    id = id
    title = 'Editar Registro'
    obj = controlModel.objects.get(id=id)
    print(obj)
    form = controlFormm()
    if request.method == 'POST':
        form = controlFormm(request.POST, instance=obj)
        if form.is_valid():
            form.save(commit=True)
            return redirect('list')
    else:
        form = controlFormm()
    return render(request, 'editar_registro.html', {'title': title, 'obj': obj, 'id':id,'form': form})


def elimiar_registro(request, id):
    id = id
    title = 'ELimiar Registro'
    ctx = controlModel.objects.get(id=id)
    ctx.delete()
        
    return redirect('list')


def login(request):
    title = 'Login'
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        user = User.objects.get(username=request.POST['username'])
        if user.check_password(requestPOST['password']):
            request.session['user_id'] = user.id
            return redirect('list')
        else:
            return HttpResponse('No logueado')
    return render(request, 'auth/login.html', {'form': form, 'title': title})



def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        return HttpResponse('Deslogueado')
