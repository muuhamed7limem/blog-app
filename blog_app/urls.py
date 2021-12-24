from django.contrib import admin
from django.urls import path, include
from articles import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first , name='first'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
