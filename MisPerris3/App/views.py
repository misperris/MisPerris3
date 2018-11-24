from .models import Usuario, Mascota
from .forms import AgregarUsuario, LoginFormulario, RestablecerPasswordForm, RestablecerPasswordMail, RegUsuario, AgregarMascota
from django import template
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

def index(request):
    lista = Mascota.objects.all()
    return render(request, "index.html", {'lista':lista})

@login_required(login_url="login")
@staff_member_required
def gestionUsuario(request):
    usuarios=User.objects.all()
    cositas=Usuario.objects.all()
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        u=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        var_rol = data.get("rol")
        if var_rol == "Normal":
            u.is_staff=False
        else:
            u.is_staff=True
        u.save()
        regDB=Usuario(nombre=data.get("nombre"),apellido=data.get("apellido"),fecha=data.get("fecha"),region=data.get("region"),ciudad=data.get("ciudad"),vivienda=data.get("vivienda"),rol=data.get("rol"),user=u)
        regDB.save()
        return redirect('clientes')
    form=AgregarUsuario()
    return render(request,"GestionarUsuario.html",{'form':form,'usuarios':usuarios,'cositas':cositas})

def ingresar(request):
    form=LoginFormulario(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("usr"),password=data.get("passwd"))
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request,"login.html",{'form':form})


@login_required(login_url="login")
def salir(request):
    logout(request)
    return redirect("/")


def recovery(request):
    form=RestablecerPasswordMail(request.POST or None)
    
    if form.is_valid():
        data=form.cleaned_data
        usuario=User.objects.get(username=data.get("username"))
        send_mail(
                'Recuperar Password',
                'Me gusta el Fortnite lo juego todo el dia esto no es Minecraft me encanta es muy bueno',
                'from@example.com',
                [usuario.email],
                html_message='Pinchando el siguiente <a href="http://localhost:8000/changepassword?user='+usuario.username+'">enlace</a> podras restablecer tu contraseña',
            )
        return redirect('login')
    return render(request,"passwdrcv.html",{'form':form})

def changepassword(request):
    form=RestablecerPasswordForm(request.POST or None)
    username=request.GET["user"]
    if username is not None:
        if form.is_valid():
            data=form.cleaned_data
            
            if data.get("nuevapass") == data.get("nuevapasscheck"):
                passwd=make_password(data.get("nuevapasscheck"))
                User.objects.filter(username=username).update(password=passwd)
                return redirect('/login/')
        return render(request,"changepassword.html",{'form':form, 'username':username})
    else:
        return redirect('/login/')


@login_required(login_url="login")
@staff_member_required
def clientes(request): 
    lista = Usuario.objects.all()
    return render(request, 'clientes.html', {'lista':lista})

@login_required(login_url="login")
@staff_member_required
def deleteuser(request,id):
    placeholder=Usuario.objects.get(id=id)
    if request.method=='POST':
        placeholder.delete()
        return redirect('clientes')
    return render(request,'deleteuser.html',{'placeholder':placeholder})

def regusr(request):
    usuarios=User.objects.all()
    cositas=Usuario.objects.all()
    form=RegUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        u=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        var_rol="Normal"
        if var_rol == "Normal":
            u.is_staff=False
        else:
            u.is_staff=True
        u.save()
        regDB=Usuario(nombre=data.get("nombre"),apellido=data.get("apellido"),fecha=data.get("fecha"),region=data.get("region"),ciudad=data.get("ciudad"),vivienda=data.get("vivienda"),user=u)
        regDB.save()
        return redirect('login')
    form=RegUsuario()
    return render(request,"regusr.html",{'form':form,'usuarios':usuarios,'cositas':cositas})

@login_required(login_url="login")
@staff_member_required
def regpet(request):
    pets=Mascota.objects.all()
    form=AgregarMascota(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Mascota(nombre=data.get("nombre"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"),pic=request.FILES['pic'])
        regDB.save()
        return redirect('mngrpet')
    form=AgregarMascota()
    return render(request,"regpet.html",{'form':form,'pets':pets})

@login_required(login_url="login")
@staff_member_required
def deletepet(request,id):
    placeholder=Mascota.objects.get(id=id)
    if request.method=='POST':
        placeholder.delete()
        return redirect('mngrpet')
    return render(request,'deletepet.html',{'placeholder':placeholder})

@login_required(login_url="login")
def adoptpets(request):  
    form=AgregarMascota(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        Mascota.objects.create(nombre=data.get("nombre"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"),pic=request.FILES['pic'])
    form=AgregarMascota()
    mascotas=Mascota.objects.all()
    paginator=Paginator(mascotas,3)

    try:
        pag=int(request.GET.get("page",1))
    except ValueError:
        pag=1

    try:
        mascotas=paginator.page(pag)
    except (InvalidPage, EmptyPage):
        mascotas=paginator.page(paginator.num_pages)
    
    contexto={"mascotas":mascotas,"form":form}
    return render(request,'adoptpet.html',contexto)

@login_required(login_url="login")
@staff_member_required
def petupdate(request,id):
    regDB=Mascota.objects.get(id=id)
    if request.method=="POST":
        form=AgregarMascota(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            regDB.nombre=data.get("nombre")
            regDB.raza=data.get("raza")
            regDB.descripcion=data.get("descripcion")
            regDB.estado=data.get("estado")
            regDB.pic=request.FILES['pic']
            regDB.save()
            return redirect("mngrpet")
    else:
        data={
            "nombre":regDB.nombre,
            "raza":regDB.raza,
            "descripcion":regDB.descripcion,
            "estado":regDB.estado
        }
        form=AgregarMascota(data)
    return render(request, "editpet.html", {"form":form})

@login_required(login_url="login")
@staff_member_required
def mngrpets(request):  
    form=AgregarMascota(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        Mascota.objects.create(nombre=data.get("nombre"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"),pic=request.FILES['pic'])
    form=AgregarMascota()
    mascotas=Mascota.objects.all()
    paginator=Paginator(mascotas,3)

    try:
        pag=int(request.GET.get("page",1))
    except ValueError:
        pag=1

    try:
        mascotas=paginator.page(pag)
    except (InvalidPage, EmptyPage):
        mascotas=paginator.page(paginator.num_pages)
    
    contexto={"mascotas":mascotas,"form":form}
    return render(request,'mngrpet.html',contexto)
