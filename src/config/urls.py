from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Doc",
        default_version="v1",
        description="Doc description",
        terms_of_service="https://smaple.com/terms/",
        contact=openapi.Contact(email="asilbek@novalab.uz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path("", include("polls.urls"), name="polls"),
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
