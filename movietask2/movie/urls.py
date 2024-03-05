from django.urls import path, include

from movie import views

app_name='movie'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('movie/<slug:c_slug>/', views.allmoviecat, name='movies_by_category'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('moviepage/', views.movie_show, name='movie_show'),
    path('allmovies/<slug:c_slug>/', views.allmoviecat, name='allmoviecat'),
    path('add/', views.add_movie, name='add_movie'),


]