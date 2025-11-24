from django.urls import path, include
from . import views

app_name = "companies"
urlpatterns = [
    path("sendemail/", views.sendmail, name="sendmail"),
    path(
        "",
        views.CompanyViewSet.as_view({"get": "list", "post": "create"}),
        name="index",
    ),
    path(
        "<int:pk>/",
        views.CompanyViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="detail",
    ),
]
