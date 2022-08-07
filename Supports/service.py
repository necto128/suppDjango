from Supports import models
from django.core.mail import send_mail
import suppDjango.settings as siting


#
def get_filter_requvests(request):
    return list(models.Requests.objects.filter(users=request.user.id,
                                               status="Active").values_list('id', flat=True))[0]


def filter_request(request):
    return models.Requests.objects.filter(
        users=request.user.id).values("id", "users", "topic", "status")


def get_request_active(pk):
    stat = models.Requests.objects.get(id=pk).status
    if stat in "Waiting" or stat in "Active":
        return True
    else:
        return False


def get_len_requvest(request):
    if len(models.Requests.objects.filter(status='Active', users=request.user.id)) > 0:
        return False
    else:
        return True


def get_request(pk):
    return models.Requests.objects.get(id=pk)


def send(stats, users_id):
    if stats == "Active":
        stats = "Активный"
    else:
        stats = "Неактивный"

    send_mail("Support",
              f"Ваш статус запроса был изменён на {stats}",
              siting.EMAIL_HOST_USER,
              [models.User.objects.get(id=users_id).email],
              fail_silently=False,
              )
