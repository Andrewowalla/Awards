from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login_user/', views.login_user, name ='login'),
    path('', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout' ),
    path('new/project', views.new_project, name='new_project'),
    path('register_user', views.register_user, name='register_user'),
    path('view_profile/<int:pk>', views.view_profile, name='view_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('projects/', views.projects, name='projects'),
    path('rate_project/<id>/', views.rate_project, name='rate_project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)