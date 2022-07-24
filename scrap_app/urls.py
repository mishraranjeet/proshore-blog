from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('blog/<int:blog_id>', views.blog_detail, name="blog_detail"),
    path('blog-delete/<int:blog_id>', views.blog_delete, name="blog_delete"),
    path('blog-edit/<int:blog_id>', views.blog_edit, name="blog_edit"),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

