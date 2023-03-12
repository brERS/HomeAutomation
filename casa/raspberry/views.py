import datetime

import psutil
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hardware_info(request):
    boot_time = datetime.datetime.fromtimestamp(
        psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")

    context = {
        'boot_time': boot_time,
    }

    return render(request, 'raspberry/pages/hardware_info.html', context)


def get_info_cpu(request):
    return HttpResponse(psutil.cpu_percent())


def get_info_memory(request):
    return HttpResponse(psutil.virtual_memory().percent)


def get_info_disk(request):
    return HttpResponse(psutil.disk_usage('/').percent)
