from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response
from Supports import serializers
from Supports import models
from .tasks import send_mailing
from Supports import service


# Create your views here.

class RequestsUsers(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        requests = service.filter_request(request)
        return Response(data=requests, status=202)

    def post(self, request):
        if service.get_len_requvest(request):
            requests_model = serializers.RequestsCreateSerializer(data=self.request.data)
            if requests_model.is_valid():
                requests_model.save()
        return redirect("requests")


class TiketsDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            id_requvest = models.Requests.objects.get(users=request.user.id, id=pk)
        except Exception:
            return redirect("requests")
        tikets = models.Tikets.objects.filter(
            request_id=id_requvest).values("id", "request", "user", "message")
        return Response(data=tikets, status=202)

    def post(self, request, pk):
        if service.get_request_active(pk):
            tikets_model = serializers.TiketsCreateSerializer(data=self.request.data)
            if tikets_model.is_valid():
                tikets_model.save()
        return redirect(f"{request.build_absolute_uri()}")


class RequestsAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        requests = models.Requests.objects.filter().values("id", "users", "topic", "status")
        return Response(data=requests, status=202)


class TiketsDetailsAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        try:
            id_requvest = models.Requests.objects.get(id=pk)
        except Exception:
            return redirect("admin/requests/")
        tikets = models.Tikets.objects.filter(
            request_id=id_requvest).values("id", "request", "user", "message")
        return Response(data=tikets, status=202)

    def post(self, request, pk):
        if service.get_request_active(pk):
            tikets_model = serializers.TiketsCreateSerializer(data=self.request.data)
            if tikets_model.is_valid():
                tikets_model.save()
        return redirect(f"{request.build_absolute_uri()}")


class UpStatRequestsAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk):
        if service.get_request(pk) is not None and len(self.request.data["status"]) > 0:
            stats = self.request.data["status"]
            requests_model = service.get_request(pk)
            requests_model.status = stats
            requests_model.save()
            send_mailing.delay(stats, requests_model.users_id)
        return redirect("admin/requests/")
