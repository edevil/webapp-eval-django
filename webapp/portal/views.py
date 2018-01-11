from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from structlog import get_logger


logger = get_logger()


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class UnprotectedView(View):
    def get(self, _request):
        logger.error('error Logging test of unprotected view', logarg='arg1')
        logger.debug('debug Logging test of unprotected view', logarg='arg2')
        logger.info('info Logging test of unprotected view', logarg='arg3')
        return HttpResponse('result')


class ProtectedView(LoginRequiredMixin, View):
    def get(self, _request):
        logger.info('Logging test of protected view', logarg='arg2')
        return HttpResponse('result')
