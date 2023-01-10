from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about-us',views.about, name='about'),
    path('game/<int:game_id>/', views.show_game, name='game')
]