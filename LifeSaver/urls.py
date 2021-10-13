from django.conf.urls import url
from django.urls import path
from .views import model_form_upload

urlpatterns = [
    path('form', view=model_form_upload)
]
