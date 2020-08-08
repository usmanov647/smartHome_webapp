from django.http import HttpResponse
from django.template import loader
from .models import Zone

# Create your views here.
def index(request):
    context = {
        'first_floor_zones': Zone.objects.filter(floor=1),
        'second_floor_zones': Zone.objects.filter(floor=2)
    }
    template = loader.get_template('usman/index.html')
    return HttpResponse(template.render(context, request))

def control(request, zone_name):
    context = {
        'zone_selected': Zone.objects.get(zone_name=zone_name),
    }
    template = loader.get_template('usman/control.html')
    return HttpResponse(template.render(context, request))