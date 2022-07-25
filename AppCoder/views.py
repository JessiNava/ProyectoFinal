from ast import Delete
import mailbox
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Create your views here.

def padre(request):
    return render(request,"AppCoder/padre.html")

def about(request):
    return render(request,"AppCoder/about.html")
 
@login_required   
def inicio(request):
   
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request,"AppCoder/inicio.html", {"url": avatares[0].imagen.url})
    #return render(request,"AppCoder/inicio.html")

def blog(request):
        if request.method=='POST':
            miFormulario=blog_formulario(request.POST)
            if miFormulario.is_valid():
                informacion= miFormulario.cleaned_data
                blog=Post(titulo=informacion['titulo'],contenido=informacion['contenido'], fecha=informacion['fecha'])
                blog.save()
                return render(request,"AppCoder/padre.html")
        else:
            miFormulario=blog_formulario()
        return render(request,"AppCoder/blog.html",{"miFormulario":miFormulario})

def leerBlog(request):
    blogs=Post.objects.all()
    contexto={"blogs":blogs}
    return render(request,"AppCoder/leerblog.html",contexto)




def perro(request):
        if request.method=='POST':
            miFormulario=PerroFormulario(request.POST)
            if miFormulario.is_valid():
                informacion= miFormulario.cleaned_data
                perro=Perro(name=informacion['name'],raza=informacion['raza'],edad=informacion['edad'])
                perro.save()
                return render(request,"AppCoder/padre.html")
        else:
            miFormulario=PerroFormulario()
        
        return render(request,"AppCoder/perros.html",{"miFormulario":miFormulario})
        

def gato(request):
    if request.method=='POST':
        miFormulario=GatoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            gato=Gato(name=informacion['name'],raza=informacion['raza'],edad=informacion['edad'])
            gato.save()
            return render(request,"AppCoder/padre.html")
    else:
        miFormulario=GatoFormulario()

    return render(request,"AppCoder/gatos.html",{"miFormulario":miFormulario})
    

def ave(request):
    if request.method=='POST':
        miFormulario=AveFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            ave=Ave(name=informacion['name'],raza=informacion['raza'],edad=informacion['edad'])
            ave.save()
            return render(request,"AppCoder/padre.html")
    else:
        miFormulario=AveFormulario()

    return render(request,"AppCoder/ave.html",{"miFormulario":miFormulario})

def buscar(request):

    # busqueda= request.GET["name"]
    # perros=Perro.objects.all()


    # if busqueda:
    #     perros= Perro.objects.filter(
    #         Q(name_icontains = busqueda) |
    #         Q(raza_icontains = busqueda)
    #     ).distict()

    # return render(request, "AppCoder/inicio.html", {"perros":perros})

    if  request.GET["name"]: #if request.method == 'Get':

          #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['name'] 
            
            perrobusq = Perro.objects.filter(name__icontains=nombre)
            
            return render(request, "AppCoder/inicio.html", {"name":perrobusq})

    else: 

          respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
    return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})
        
def leerPerros(request):
    perros=Perro.objects.all()
    contexto={"perros":perros}
    return render(request,"AppCoder/leerPerros.html",contexto)


def eliminarPerro(request,perro_nombre):
    perro= Perro.objects.get(name=perro_nombre)
    perro.delete()
    perros=Perro.objects.all()
    contexto={"perro":perros}
    return render(request,"AppCoder/leerPerros.html",contexto)

def editarPerro(request,perro_nombre):
    perro=Perro.objects.get(name=perro_nombre)
    if request.method== "POST":
        miFormulario=PerroFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            perro.name=informacion['name']
            perro.raza=informacion['raza']
            perro.edad=informacion['edad']
            perro.save()
            return render(request,"AppCoder/padre.html")
    else:
        miFormulario=PerroFormulario(initial={"name":perro.name, "raza":perro.raza, "edad":perro.edad})
    return render(request,"AppCoder/editarPerro.html",{"miFormulario":miFormulario,"perro_nombre":perro_nombre})

class GatoList(ListView):
    model= Gato
    template_name="AppCoder/gatos_list.html"
    
class GatoDetail(DetailView):
    model= Gato
    template_name="AppCoder/gato_detail.html"
    
class GatoCreacion(CreateView):
    model=Gato
    success_url=reverse_lazy('List')
    fields=['name','raza','edad']
    
class GatoUpdate(UpdateView):
    model=Gato
    success_url=reverse_lazy('List')
    fields=['name','raza','edad']
    
    
class GatoDelete(DeleteView):
    model=Gato
    success_url=reverse_lazy('List')



def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contra)
            
            
            if user is not None:
                login(request, user)
                
                return render(request,"AppCoder/inicio.html", {"mensaje": f"Bienvenido{usuario}"})
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje": "Error, datos invalidos"})
            
        else:
            
                return render(request, "AppCoder/inicio.html", {"mensaje" : "Error, formulario erroneo"})
            
    form = AuthenticationForm()
    
    return render(request, "AppCoder/login.html", {'form': form})         




def register(request):
    
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html" , {"mensaje": "Usuario Creado"})
        
    else:
        form = UserCreationForm()
        
    return render(request, "AppCoder/registro.html" , {"form" : form})            



@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.first_name= informacion['first_name']
                  usuario.last_name= informacion['last_name']
                  usuario.save()
            
                  return render(request, "AppCoder/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "AppCoder/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})




