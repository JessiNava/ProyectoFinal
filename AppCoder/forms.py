from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blog_formulario(forms.Form):
    titulo=forms.CharField()
    contenido=forms.CharField()
    fecha=forms.DateField()

class PerroFormulario(forms.Form):
    name=forms.CharField()
    raza=forms.CharField()
    edad=forms.IntegerField()

class GatoFormulario(forms.Form):
    name=forms.CharField()
    raza=forms.CharField()
    edad=forms.IntegerField()
    

class AveFormulario(forms.Form):
    name=forms.CharField()
    raza=forms.CharField()
    edad=forms.IntegerField()
    

class UserRegisterForm(UserCreationForm):
    password1: forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2: forms.CharField(label='Repetir Contraseña', widget= forms.PasswordInput) 
    
    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}   


class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(label='Ingresa tu nombre')
    last_name= forms.CharField(label='Ingresa tu apellido')

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

