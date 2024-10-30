from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from objects.forms import ObjectForm, MeterForm, FlowMeterSertificateForm
from objects.models import Organization, Object, Meter, FlowMeterSertificate, ObjectType
from orifice_plate.models import OrificePlate


# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    user_organization = request.user.profile.organization
    type_objects = ObjectType.objects.all()
    print(type_objects)
    context = {
        "user_organization" : user_organization,
        "type_objects" : type_objects
    }
    return render(request, 'index.html', context)


def get_organizations(request):
    user_organization = request.user.profile.organization
    organizations = Organization.objects.all()
    context = {
        "user_organization" : user_organization,
        "organizations" : organizations
    }
    return render(request, 'organizations.html', context)


@login_required
def get_objects(request):
    user_organization = request.user.profile.organization
    print(user_organization)
    if user_organization is None:
        objects = Object.objects.all().order_by('name')
        #my_filter = ObjectFilter(request.GET, queryset=objects)
        #objects = my_filter.qs
    else:
        objects = Object.objects.filter(organization__name=user_organization).order_by('name')
        #my_filter = ObjectFilter(request.GET, queryset=objects)
        #objects = my_filter.qs

    paginator = Paginator(objects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "objects" : page_obj,
        "object_count" : len(objects),
        "user_organization" : user_organization
    }

    return render(request, 'objects/objects_list.html', context)


@login_required
def object_details(request, pk):
    user_organization = request.user.profile.organization
    object = get_object_or_404(Object, pk=pk)
    meters = Meter.objects.filter(object=object).order_by('meter_id')
    amount = len(meters)
    context = {
        "object": object,
        "user_organization": user_organization,
        "meters": meters,
        "amount": amount,
    }
    return render(request, 'objects/object_details.html', context)


@login_required
def add_object(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yangi obyekt qo`shildi!')
            return redirect('objects')
    else:
        form = ObjectForm()

    return render(request, 'objects/add_object.html', {'form': form})


@login_required
def edit_object(request, pk):
    object = get_object_or_404(Object, pk=pk)
    if request.method == 'POST':
        form = ObjectForm(request.POST, instance=object)
        form.organization = request.user.profile.organization
        if form.is_valid():
            print("ok")
            form.save()
            return redirect('object_details', pk=pk)
    else:
        form = ObjectForm(instance=object)

    return render(request, 'objects/edit_object.html', {'form': form, 'object': object})


@login_required
def delete_object(request, pk):
    object = get_object_or_404(Object, pk=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('objects')
    else:
        return render(request, 'objects/delete_object.html', {'object': object})


@login_required
def get_meters(request):
    user_organization = request.user.profile.organization
    print(user_organization)
    if user_organization is None:
        meters = Meter.objects.all().order_by('organization')
        #my_filter = MeterFilter(request.GET, queryset=meters)
        #meters = my_filter.qs
    else:
        meters = Meter.objects.all().filter(organization__name=user_organization).order_by('meter_id')
        #my_filter = MeterFilter(request.GET, queryset=meters)
        #meters = my_filter.qs

    paginator = Paginator(meters, 5)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {
        "meters": page_obj,
        "amount": len(meters),
        "user_organization": user_organization
    }

    return render(request, 'meters/meters_list.html', context)


def add_meter(request, pk):
    object_instance = get_object_or_404(Object, pk=pk)
    if request.method == 'POST':
        form = MeterForm(request.POST)
        if form.is_valid():
            meter = form.save(commit=False)
            meter.object = object_instance
            form.save()
            return redirect('object_details', pk = object_instance.pk)
    else:
        form = MeterForm()
    return render(request, 'meters/add_meter.html', {'form': form})


def edit_meter(request, pk):
    meter = get_object_or_404(Meter, pk=pk)
    if request.method == 'POST':
        form = MeterForm(request.POST, instance=meter)
        if form.is_valid():
            form.save()
            return redirect('meter_details', pk=pk)
        else:
            print("ERROR")
    else:
        form = MeterForm(instance=meter)
    context = {
        'form': form,
        'meter': meter,
    }
    return render(request, 'meters/edit_meter.html', context)


@login_required
def delete_meter(request, pk):
    meter_instance = get_object_or_404(Meter, pk=pk)
    if request.method == 'POST':
        meter_instance.delete()
        return redirect('object_details', pk=meter_instance.object.id)
    else:
        return render(request, 'meters/delete_meter.html', {'meter_instance': meter_instance})


@login_required
def meter_details(request, pk, ):
    user_organization = request.user.profile.organization
    meter = get_object_or_404(Meter, pk=pk)

    orifice_plates = OrificePlate.objects.filter(meter=meter).order_by('-installed_date')
    sertificates = FlowMeterSertificate.objects.filter(meter=meter).order_by('date_start')

    context = {

        "user_organization": user_organization,

        "meter": meter,
        "orifice_plates": orifice_plates,
        "sertificates": sertificates,
        "amount": len(orifice_plates)
    }
    return render(request, 'meters/meter_details.html', context)


def add_flowmeter_sertificate(request, pk):
    meter = get_object_or_404(Meter, pk=pk)
    if request.method == 'POST':
        form = FlowMeterSertificateForm(request.POST, request.FILES)  # Добавляем request.FILES для загрузки файлов
        if form.is_valid():
            certificate = form.save(commit=False)  # Сохраняем форму без сохранения в базу данных
            certificate.meter = meter  # Присваиваем meter вручную
            certificate.save()  # Сохраняем объект в базу данных
            return redirect('meter_details', pk=meter.pk)
        else:
            print("Форма не валидна:", form.errors)  # Выводим ошибки для отладки
    else:
        form = FlowMeterSertificateForm()

    return render(request, 'meters/add_flowmeter_sertificate.html', {'form': form, 'meter': meter})


def edit_flowmeter_sertificate(request, pk):
    sertificate_instance = get_object_or_404(FlowMeterSertificate, pk=pk)
    if request.method == 'POST':
        form = FlowMeterSertificateForm(request.POST, request.FILES, instance=sertificate_instance)
        if form.is_valid():
            form.save()
            return redirect('meter_details', pk=sertificate_instance.meter.id)
        else:
            print("Форма не валидна:", form.errors)
    else:
        form = FlowMeterSertificateForm(instance=sertificate_instance)
    context = {
        'form': form,
        'sertificate_instance': sertificate_instance,
    }
    return render(request, 'meters/edit_flowmeter_sertificate.html', context)


@login_required
def delete_flowmeter_sertificate(request, pk):
    sertificate_instance = get_object_or_404(FlowMeterSertificate, pk=pk)
    if request.method == 'POST':
        sertificate_instance.delete()
        return redirect('meter_details', pk=sertificate_instance.meter.id)
    else:
        return render(request, 'meters/delete_flowmeter_sertificate.html', {'sertificate_instance': sertificate_instance})


def get_all_sertificates(request):
    user_organization = request.user.profile.organization
    if user_organization is None:
        sertificates = FlowMeterSertificate.objects.all().order_by('meter')

    else:
        sertificates = FlowMeterSertificate.objects.all().filter(meter__organization__name=user_organization).order_by('meter')

    paginator = Paginator(sertificates, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'sertificates': sertificates,
        'user_organization': user_organization,
        'amount': len(sertificates)
    }
    return render(request, 'meters/sertificate_list.html', context)


def get_active_sertificates(request):
    user_umg = request.user.profile.umg
    if user_umg is None:
        sertificate = Flow_meter_sertificate.objects.all().filter(is_active='Amalda').order_by('object')
    else:
        sertificate = Flow_meter_sertificate.objects.all().filter(umg__name=user_umg, is_active='Amalda').order_by('object')
    amount = len(sertificate)
    paginator = Paginator(sertificate, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'meters/sertificate_list.html',
                  {'page_obj': page_obj, 'sertificate': sertificate, 'user_umg': user_umg, 'amount':amount})

def get_not_active_sertificates(request):
    user_umg = request.user.profile.umg
    if user_umg is None:
        sertificate = Flow_meter_sertificate.objects.all().filter(is_active='Amalda emas').order_by('object')
    else:
        sertificate = Flow_meter_sertificate.objects.all().filter(umg__name=user_umg, is_active='Amalda emas').order_by('object')
    amount = len(sertificate)
    paginator = Paginator(sertificate, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'meters/sertificate_list.html',
                  {'page_obj': page_obj, 'sertificate': sertificate, 'user_umg': user_umg, 'amount':amount})