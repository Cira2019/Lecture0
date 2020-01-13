from django.urls import path
from django.conf.urls import url
from . import views
from .views import CountryAutocomplete

app_name='SIA'
urlpatterns=[
	path('create',views.create,name='create'),
	path("upload",views.upload,name="upload"),
	url(
        r'^country-autocomplete/$',
        CountryAutocomplete.as_view(),
        name='country-autocomplete',
    ),
]