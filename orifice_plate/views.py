from django.shortcuts import render, get_object_or_404, redirect

from objects.models import Meter
from orifice_plate.forms import AddOrificePlateForm
from orifice_plate.models import OrificePlate


def get_orifice_plates(request):
    user_organization = request.user.profile.organization
    if user_organization is None:
        orifice_plates = OrificePlate.objects.all().order_by('meter')
        #my_filter = MeterFilter(request.GET, queryset=meters)
        #meters = my_filter.qs
    else:
        orifice_plates = OrificePlate.objects.all().filter(meter__organization__name=user_organization).order_by('meter')
        #my_filter = MeterFilter(request.GET, queryset=meters)
        #meters = my_filter.qs
    print(orifice_plates)
    #paginator = Paginator(meters, 10)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    context = {
        "orifice_plates": orifice_plates,
        "amount": len(orifice_plates),
        "user_organization": user_organization
    }

    return render(request, 'orifice_plates/orifice_plates_list.html', context)

# Create your views here.
def add_orifice_plate(request, pk):
    meter = get_object_or_404(Meter, pk=pk)
    if request.method == 'POST':
        form = AddOrificePlateForm(request.POST)
        if form.is_valid():
            orifice_plate = form.save(commit=False)
            orifice_plate.meter = meter
            orifice_plate.save()
            return redirect('meter_details', pk=meter.pk)
    else:
        form = AddOrificePlateForm()
    return render(request, 'orifice_plates/add_orifice_plate.html', {'form': form})
