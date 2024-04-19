from django.urls import path, include   # Importamos las funciones path e include.
from rest_framework.routers import DefaultRouter    
from .views import (
    DocumentInteractionView, DocumentoViewSet, UserViewSet, TemplateListViewSet, 
    FileUploadViewSet, GenerateTextView, DocumentSummaryView, 
    TextClassificationView, ChatView) 
from rest_framework.documentation import include_docs_urls    # Importamos la función include_docs_urls.

# Aquí estamos creando un objeto router que nos permitirá generar las rutas de forma automática.
router = DefaultRouter()    # Creamos un objeto router.
router.register(r'documentos', DocumentoViewSet)    # Registramos la ruta /documentos/ para el viewset DocumentoViewSet.
router.register(r'usuarios', UserViewSet)   # Registramos la ruta /usuarios/ para el viewset UserViewSet.
router.register(r'templates', TemplateListViewSet, basename='template') # Registramos la ruta /templates/ para el viewset TemplateListViewSet.
router.register(r'upload', FileUploadViewSet, basename='file-upload')    # Registramos la ruta /upload/ para el viewset FileUploadViewSet.
#router.register(r'chat', ChatView, basename='chat')    # Registramos la ruta /chat/ para el viewset ChatRoomView.
#router.register(r'messages', ChatMessageView, basename='chat-message')    # Registramos la ruta /messages/ para el viewset ChatMessageView.

# Aquí estamos extendiendo urlpatterns con las nuevas rutas.
urlpatterns = [
    path('', include(router.urls)),   # Añadimos las rutas generadas por el router.
    path('home/', include(router.urls)),    # Añadimos la ruta /home/ para que sea un alias de /.
    path('chat/', ChatView.as_view(), name='chat'),
    path('generate-text/', GenerateTextView.as_view(), name='generate-text'),   # Añadimos la ruta /generate-text/ para la vista GenerateTextView.
    path('summarize-document/', DocumentSummaryView.as_view(), name='summarize-document'),  # Añadimos la ruta /summarize-document/ para la vista DocumentSummaryView.
    path('classify-text/', TextClassificationView.as_view(), name='classify-text'), # Añadimos la ruta /classify-text/ para la vista TextClassificationView.
    path('doc/', include_docs_urls(title='Documentación de la API')),    # Añadimos la ruta /doc/ para la documentación de la API.
    path('interactive-doc/', DocumentInteractionView.as_view(), name='interactive-doc'),    # Añadimos la ruta /interactive-doc/ para la vista DocumentInteractiveView.
]
