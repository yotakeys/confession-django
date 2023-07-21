from django.urls import path
from .views import Login, Register, ConfessionList, ConfessionUrl, CreateConfession
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('', ConfessionList.as_view(), name="confessionList"),
    path('create/', CreateConfession.as_view(), name="confessionCreate"),
    path('<str:slug>/', ConfessionUrl.as_view(), name="confessionUrl")
]
