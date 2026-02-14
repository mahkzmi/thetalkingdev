from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", include("contact.urls")),
    path("blog/", include("blog.urls")),
    path("projects/", include("projects.urls")),
    path("", include("core.urls")),
    path('services/', include('services.urls')),

]
