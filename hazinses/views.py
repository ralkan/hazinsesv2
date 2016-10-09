import simplejson
from django.utils import timezone
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from models import SNSMessage, UserEmailProfile


class SNSMessageView(generic.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(SNSMessageView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        json = request.raw_post_data
        js = simplejson.loads(json)
        message = simplejson.loads(js["Message"])
        SNSMessage.objects.create(subject="title", message=request.POST)
        mail = message['mail']['destination'][0]
        useremail = UserEmailProfile.objects.get(user__email=mail)
        if message['notificationType'] == "Bounce":
            useremail.not_send_mail = timezone.now() + timezone.timedelta(
                days=settings.BOUNCE_TIMEDELTA)
        elif message['notificationType'] == "Complaint":
            useremail.not_send_mail = timezone.now() + timezone.timedelta(
                days=settings.COMPLAINT_TIMEDELTA)
        useremail.save()
        return HttpResponse('ok')
