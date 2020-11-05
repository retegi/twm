from django.contrib import admin
from django.urls import path
#INCLUIDOS
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path('', include('applications.home.urls')),
    re_path('blog/', include('applications.blog.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


