from django.urls import path
from .views import testView

urlpatterns = [
    path('', view=testView, name="test")
]
