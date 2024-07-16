import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.views.generic import TemplateView

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
    path('hello/', include('hello.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),

]
