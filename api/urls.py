from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('publishers', views.PublisherViewSet)
router.register('books', views.BookViewSet)

schema_view = get_swagger_view(title='Books API')

app_name = 'api'
urlpatterns = [
    path('', schema_view, name='swagger-api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls), name='router-api'),
    path('counters/', views.CountersView.as_view(), name='counters'),

    # Route TemplateView to serve Swagger UI template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]
