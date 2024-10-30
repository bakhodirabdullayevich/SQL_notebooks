from django.shortcuts import render, get_object_or_404, redirect

from objects.models import Meter
from restored_volume.forms import RestoredVolumeForm
from restored_volume.models import Volume, Period

'''def get_restored_volume(request):
    user_organization = request.user.profile.organization
    if user_organization is None:
        restored_volumes = Volume.objects.all().order_by('meter')

    else:
        restored_volumes = Volume.objects.filter(meter__organization__name=user_organization).order_by('meter')
    context = {
        'user_organization': user_organization,
        'restored_volumes': restored_volumes,
    }
    return render(request, 'restored_volume/restored_volume_list.html', context)'''



def get_restored_volume(request):
    user_organization = request.user.profile.organization
    restored_volumes = Volume.objects.all()  # По умолчанию берём все

    # Получаем параметры месяца и года из GET-запроса
    month = request.GET.get('month')
    year = request.GET.get('year')

    if user_organization is not None:
        restored_volumes = restored_volumes.filter(meter__organization__name=user_organization)

    # Фильтрация по месяцу и году, если они указаны
    if month and year:
        try:
            month = int(month)
            year = int(year)
            restored_volumes = restored_volumes.filter(month__year=year, month__month=month)
        except ValueError:
            pass  # Игнорируем ошибки преобразования

    restored_volumes = restored_volumes.order_by('meter')

    # Список месяцев для выпадающего списка
    months = list(range(1, 13))

    context = {
        'user_organization': user_organization,
        'restored_volumes': restored_volumes,
        'selected_month': month,  # Не преобразуем в строку
        'selected_year': year,     # Не преобразуем в строку
        'months': months,          # Передаем список месяцев в контекст
    }
    return render(request, 'restored_volume/restored_volume_list.html', context)


def add_restored_volume(request, pk):
    meter = get_object_or_404(Meter, pk=pk)
    if request.method == 'POST':
        form = RestoredVolumeForm(request.POST)
        if form.is_valid():
            restored_volume = form.save(commit=False)  # Сохраняем форму без сохранения в базу данных
            restored_volume.meter = meter  # Присваиваем meter вручную
            restored_volume.save()  # Сохраняем в базу данных
            return redirect('index')
        else:
            print("Форма не валидна:", form.errors)  # Выводим ошибки для отладки
    else:
        form = RestoredVolumeForm()

    return render(request, 'restored_volume/add_restored_volume.html', {'form': form, 'meter': meter})


def get_meters_with_restored_volumes(request):
    user_organization = request.user.profile.organization
    context = {
        "user_organization": user_organization,
    }

    return render(request, 'restored_volume/meters_with_restored_volumes.html', context)


'''def get_meters_with_restored_volumes(request):
    user_organization = request.user.profile.organization
    data = Volume.objects.select_related('meter').values(
        'meter_id',
        'meter__meter_id',
        'meter__object__name',
        'meter__name',
        'restored_volume',
        'month').order_by('meter__name', 'month')
    for entry in data:
        print(f"ID: {entry['meter_id']}, Meter: {entry['meter__name']}, Month: {entry['month']}, Volume: {entry['restored_volume']}")
    if user_organization is None:
        meters = Meter.objects.all().order_by('organization')
    else:
        meters = Meter.objects.all().filter(organization__name=user_organization).order_by('meter_id')

    context = {
            "meters": meters,
            "amount": len(meters),
            "user_organization": user_organization,
            "data": data
        }

    return render(request, 'restored_volume/meters_with_restored_volumes.html', context)'''

def input_volume(request, pk):
    pass
    '''
    user_organization = request.user.profile.organization

    if request.method == 'POST':
    '''


def calendar(request):
    return render(request, 'calendar.html')