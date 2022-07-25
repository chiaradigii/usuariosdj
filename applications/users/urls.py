from django.urls import path


from . import views

app_name = "users_app"

urlpatterns = [
    
    #pagina de inicio
    path("signup/",
     views.UserRegisterViewView.as_view(),
     name='signup',
     ),
    path("login/",
     views.UserLogin.as_view(),
     name='login',
     ),
     path("logout/",
     views.logoutView.as_view(),
     name='logout',
     ),
     path("update-password/",
     views.UpdatePassword.as_view(),
     name='updatePassword',
     ),
     path("user-verification/<pk>/",
     views.CodeVerificationView.as_view(),
     name='userValidation',
     ),
   
]