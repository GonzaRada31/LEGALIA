from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppLegal.views import home_view    # Importamos la vista home_view.
#from AppLegal.views import GenerateTextView, DocumentSummaryView, TextClassificationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('AppLegal.urlsapp')),  # Organiza bajo el prefijo 'api/',
    path('', home_view, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
