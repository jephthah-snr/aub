from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from aubcotonou import settings
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import Static_Sitemap


sitemaps = {
'posts': Static_Sitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('dashboard/', include('student_management_app.urls')),
    path('timetable/', include('timetable.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

