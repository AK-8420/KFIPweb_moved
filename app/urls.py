from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import TopView, GameView, WakeUP

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('about/', TopView.as_view()),
    path('contact/', TopView.as_view()),
    path('information/<pk>/', TopView.as_view()),
    path('games/', GameView.as_view(), name='games'),
    path('games/<pk>/', GameView.as_view()),
    path('login/', TopView.as_view()),
    path('scheduler/', WakeUP),
]
urlpatterns += staticfiles_urlpatterns()