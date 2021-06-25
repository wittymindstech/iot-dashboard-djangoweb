from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('addIOTDevice/', views.addDevice, name='addDevice'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)