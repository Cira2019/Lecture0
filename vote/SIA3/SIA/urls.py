from django.urls import path
from . import views

app_name='SIA'
urlpatterns=[
	path('create',views.create,name='create'),
	path("upload",views.upload,name="upload"),

]