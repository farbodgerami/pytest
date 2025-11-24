from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .serializer import *
from .models import *
from rest_framework.pagination import PageNumberPagination
from django.urls import reverse
from django.test import Client
import json


from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view(["POST"])
# def credentialcheck(request):
#     return Response({"message": "Hello, world!"})
from django.core.mail import send_mail


@api_view(["POST"])
def sendmail(request):

    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="fb.gerami@gmail.com",
        recipient_list=["fb.gerami@gmail.com"],
    )
    return Response(
        {"status": "success", "information": "email sent successfully"}, status=200
    )


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    # print(reverse("companies:index"))
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination

    # if we want to use that reverse method:
    # def list(self, request, *args, **kwargs):
    #     companies_url = "http://127.0.0.1:8000/companies/"
    #     client = Client()
    #     response = client.get(companies_url)
    #     print(response)
    #     print(json.loads(response.content))
    #     print(reverse("companies:index"))
    #     return super().list(request, *args, **kwargs)
