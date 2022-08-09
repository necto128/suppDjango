from supports import models


def records_request(request):
    return models.Request.objects.filter(
        creator=request.user.id).values("id", "creator", "topic", "status")


def has_activity_request(pk):
    stat = models.Request.objects.get(id=pk).status
    if stat == "Active":
        return True
    else:
        return False


def checking_for_activity_request(request):
    if models.Request.objects.filter(status='Active', creator=request.user.id).exists():
        return False
    else:
        return True


def get_request(pk):
    return models.Request.objects.get(id=pk)
