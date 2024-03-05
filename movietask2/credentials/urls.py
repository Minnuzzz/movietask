from django.urls import path, include


from credentials import views
app_name='credentials'

urlpatterns = [

   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('moviepage/',views.moviepage,name='moviepage'),
   path('profile/', views.profile, name='profile'),
   path('save_profile/',views.save_profile, name='save_profile')
]
