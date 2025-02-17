from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class SecureMixin:
    @method_decorator(login_required(login_url='/login/', redirect_field_name=None))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)