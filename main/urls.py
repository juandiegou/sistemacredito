from django.urls import path

from . import views

app_name='main'
urlpatterns = [
    path(r'', views.Prestamistas.as_view(), name='prestamistas'),
    path('edit/<int:ci>/',views.PrestamistaEdit.editing , name='edit' )
]