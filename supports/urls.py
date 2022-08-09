from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from supports import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("admin/requests/", views.RequestsAdmin.as_view(), name="admin/requests/"),
    path("admin/requests/<int:pk>/", views.TicketsDetailsAdmin.as_view()),
    path("admin/requests/<int:pk>/update/", views.UpStatRequestsAdmin.as_view()),
    path("requests/", views.RequestsUser.as_view(), name="requests"),
    path("requests/<int:pk>/", views.TicketsDetails.as_view()),

]
