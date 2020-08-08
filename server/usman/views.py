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

def temperature(request, zone_name):
    return HttpResponse('Temperature control page for zone {}'.format(zone_name))

def lighting(request, zone_name):
    return HttpResponse('Lighting control page for zone {}'.format(zone_name))