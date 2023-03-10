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
    t = threading.Thread(target=start_water_flow)
    t.start()


def start_water_flow():

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(18, GPIO.OUT)

    GPIO.output(18, False)

    for value in range(0, 101):
        cache.set('water_long_task_progress', value, timeout=None)
        sleep(.6)

    GPIO.output(18, True)


def status_water_flow(request):

    if cache.get('water_long_task_progress') is None:
        run_water_flow()
    return HttpResponse(int(cache.get('water_long_task_progress')))


def abort_water_flow(request):

    GPIO.output(18, True)
    return HttpResponse(int(True))
