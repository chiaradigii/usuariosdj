from django.urls import path


from . import views

app_name = "users_app"

urlpatterns = [
    
    #pagina de inicio
    path("signup/",
     views.UserRegisterViewCreateView.as_view(),
     name='signup',
     ),
   
]