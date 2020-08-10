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
    zone_selected = Zone.objects.get(zone_name=zone_name)

    if request.method == 'POST':
        temp_set = int(request.POST['temp_set'])
        if 15 <= temp_set <= 30:
            zone_selected.temperature_set = temp_set
            zone_selected.save()
    context = {
        'zone_selected': zone_selected
    }
    template = loader.get_template('usman/control.html')
    return HttpResponse(template.render(context, request))