import threading
from time import sleep

import RPi.GPIO as GPIO
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def subnav():
    return {
        'home': {
            'title': 'Home',
            'url': 'home',
            'icon': 'bi-house-fill',
        },
        'water': {
            'title': 'Água',
            'url': 'water',
            'icon': 'bi-droplet-half',
        },
        'light': {
            'title': 'Luzes',
            'url': 'light',
            'icon': 'bi-lightbulb',
        },
    }


def index(request):

    cache.delete('water_long_task_progress')
    context = {
        'tabs': subnav(),
        'content':  {
            'info': {
                'home': {
                    'content': '''
                        Navegue pelo menu acima para acessar as funcionalidades
                        do sistema.
                    ''',
                    'subcontent': 'Descubra o que pode ser feito por você!',
                },
            },
        },
        'home': True,
    }
    return render(request, 'automation/pages/home.html', context)


def water(request):

    context = {
        'tabs': subnav(),
        'content':  {
            'info': {
                'agua': {
                    'content': '''
                        Bora colocar água fresquinha no potinho do baby dogs e
                        deixar ele hidratado e feliz!
                    ''',
                    'subcontent': 'A torneira será aberta por 1 minuto.',
                    'button': 'waterflow',
                },
            },
        },
        'home': False,
    }
    return render(request, 'automation/pages/home.html', context)


def light(request):
    context = {
        'tabs': subnav(),
        'content':  {
            'info': {
                'light': {
                    'content': '''
                        Em construção...
                    ''',
                    'subcontent': 'Em breve você poderá controlar as luzes da casa!',
                },
            },
        },
        'home': False,
    }
    return render(request, 'automation/pages/home.html', context)


def run_water_flow():
    t = threading.Thread(target=start_water_flow, name='water_flow')
    t.start()


def start_water_flow():

    global running_water_flow

    running_water_flow = True

    water_task_progress = 0

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(18, GPIO.OUT)

    GPIO.output(18, False)

    while running_water_flow:
        water_task_progress += 1
        cache.set(
            'water_long_task_progress',
            water_task_progress,
            timeout=None
        )
        sleep(.6)

        if water_task_progress >= 100:
            running_water_flow = False

    GPIO.output(18, True)


def check_tread_status():

    tread_status = False

    for t in threading.enumerate():
        if t.name == 'water_flow':
            tread_status = True
            break

    return tread_status


def status_water_flow(request):

    if not check_tread_status():
        run_water_flow()

    return HttpResponse(int(cache.get('water_long_task_progress')))


def abort_water_flow(request):

    global running_water_flow

    running_water_flow = False

    sleep(1)

    if not check_tread_status():
        return HttpResponse(int(True))
    else:
        return HttpResponse(int(False))
