from django.urls import path
from AppCoder import views
from AppCoder.forms import PerroFormulario
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.padre),
    path('inicio/',views.inicio, name="Inicio"),
    path('perros/',views.perro, name="Perros" ),
    path('gatos/',views.gato, name="Gatos" ),
    path('aves/',views.ave, name="Aves" ),
    path('buscar/',views.buscar,name="Busqueda"),
    path('leerPerros/',views.leerPerros, name="leerPerros"),
    path('eliminarPerro/<perro_nombre>/', views.eliminarPerro, name="eliminarPerro"),
    path('editarPerro/<perro_nombre>/',views.editarPerro, name="editarPerro"),
    path('gatos/list/', views.GatoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.GatoDetail.as_view(), name='Detail'),
    path(r'^nuevo$',views.GatoCreacion.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$',views.GatoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.GatoDelete.as_view(), name='Delete'),
    path('login/',views.login_request, name = "Login"),
    path('register/', views.register, name = "Register"),
    path('logout',LogoutView.as_view(template_name = 'AppCoder/logout.html'), name = 'Logout'),
    path('editar_perfil/', views.editarPerfil, name='EditarPerfil'),
    path('about', views.about, name='About'),
    path('blog/',views.blog, name="Publicar blog"),
    path('leerblog', views.leerBlog, name="Blog")
    
    ]
