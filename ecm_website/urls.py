# C:\Users\Mohammed\Documents\ECM\ecm_website\urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # Only if you still use TemplateView for some pages
from django.conf import settings
from django.conf.urls.static import static
from parts.views import InquiryCreateView, home_view # Import your specific views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), # Use the function-based home_view from parts.views
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('inquiry/', InquiryCreateView.as_view(), name='inquiry'), # Use the InquiryCreateView
    path('parts/', include('parts.urls')), # Link to your parts app URLs
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)