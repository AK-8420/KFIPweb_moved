from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import TopView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
]
urlpatterns += staticfiles_urlpatterns()