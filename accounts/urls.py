from django.urls import path
from . import views
from .views import signup, CustomLoginView
from django.contrib.auth.views import LogoutView
from .views import current_user

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('me/', current_user, name='current_user'),

]
