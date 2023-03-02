from django.urls import path
from srcpt import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('contact',views.Contact,name="contact"),
    path('about/',views.About,name="about"),
    path('blog/',views.Blog,name="blog"),
    path('add_blog',views.Add_Blog,name="add_blog"),
    path('mssg',views.Mssg,name="mssg"),
    path('signup/', views.Signup, name="signup"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
]
