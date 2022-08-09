from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response
from supports import serializers
from supports import models
from .tasks import send_mailing
from supports import service_view


# Create your views here.

class RequestsUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        requests = service_view.records_request(request)
        return Response(data=requests, status=202)

    def post(self, request):
        if service_view.checking_for_activity_request(request):
            requests_model = serializers.RequestCreateSerializer(data=self.request.data)
            if requests_model.is_valid():
                requests_model.save()
        return redirect("requests")


class TicketsDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            id_request = models.Request.objects.get(creator=request.user.id, id=pk)
        except Exception:
            return redirect("requests")
        tickets = models.Ticket.objects.filter(
            request_id=id_request).values("id", "request", "user", "message")
        return Response(data=tickets, status=202)

    def post(self, request, pk):
        if service_view.has_activity_request(pk):
            ticket_model = serializers.TicketCreateSerializer(data=self.request.data)
            if ticket_model.is_valid():
                ticket_model.save()
        return redirect(f"{request.build_absolute_uri()}")


class RequestsAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        requests = models.Request.objects.filter().values("id", "creator", "topic", "status")
        return Response(data=requests, status=202)


class TicketsDetailsAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        try:
            model_request = models.Request.objects.get(id=pk)
        except Exception:
            return redirect("admin/requests/")
        ticket = models.Ticket.objects.filter(
            request_id=model_request).values("id", "request", "user", "message")
        return Response(data=ticket, status=202)

    def post(self, request, pk):
        if service_view.has_activity_request(pk):
            ticket_model = serializers.TicketCreateSerializer(data=self.request.data)
            if ticket_model.is_valid():
                ticket_model.save()
        return redirect(f"{request.build_absolute_uri()}")


class UpStatRequestsAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk):
        if service_view.get_request(pk) and self.request.data["status"] in ("Active", "Disabled"):
            stats = self.request.data["status"]
            request_model = service_view.get_request(pk)
            request_model.status = stats
            request_model.save()
            send_mailing.delay(stats, request_model.creator)
        return redirect("admin/requests/")
