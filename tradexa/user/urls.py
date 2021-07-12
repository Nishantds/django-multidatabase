from django.urls import path


from . import views

urlpatterns = [
    path('', views.sign_up, name="sign"),
     path('login', views.login, name="login"),

    path('post', views.post_up, name="post_up"),
    path('logout', views.user_logout, name="logout"),
    
]
