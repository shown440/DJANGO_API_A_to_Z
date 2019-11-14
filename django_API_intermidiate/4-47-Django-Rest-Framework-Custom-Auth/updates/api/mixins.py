from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CSRFExemptionMixin(object):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        # dispatch = csrf token for all methods [GET, POST, PUT, DELETE, etc...]
        return super().dispatch(*args, **kwargs)