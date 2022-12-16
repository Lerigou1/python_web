from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("clara", views.clara, name="clara"),
  path("biel", views.biel, name="biel"),
  path("<str:name>", views.greet, name="greet")
]
