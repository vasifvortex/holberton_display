from django.urls import path
from .views import display_events
from .views import upload_picture
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('events/', view=display_events, name='display_events'),
    path('upload/', view=upload_picture, name='upload_picture'),
    path('admin/',view=upload_picture, name='upload_picture')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)