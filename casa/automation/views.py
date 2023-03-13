import threading
from time import sleep

import RPi.GPIO as GPIO
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from .models import Banner, SubNav, SubNavContent

# Create your views here.


def banner():

    banner = Banner.objects.get_active().first()

    return {
        'title': banner.title,
        'title_highlight': banner.title_highlight,
        'title_finish': banner.title_finish,
        'subtitle': banner.subtitle,
    }


def subnav():

    info_db = SubNav.objects.get_active().all()

    subnav = {}

    for nav in info_db:
        subnav.update({
            nav.title: {
                'title': nav.title,
                'url': nav.url,
                'icon': nav.icon
            }
        })

    return subnav


def subnav_content(subnav_page):

    contents_page = SubNavContent.objects.get_active().filter(title=subnav_page)

    info = {}

    for content in contents_page:
        info.update({
            content.id: {
                'content': content.content,
                'subcontent': content.subcontent,
                'button': content.function_button,
            }
        })

    return info


def index(request):

    page = 'Home'
    context = {
        'banner': banner(),
        'tabs': subnav(),
        'content':  {
            'info': subnav_content(page),
        },
        'is_home': True,
        'additional_js': False,
    }
    return render(request, 'automation/pages/home.html', context)


def water(request):

    page = 'Água'
    context = {
        'banner': banner(),
        'tabs': subnav(),
        'content':  {
            'info': subnav_content(page),
        },
        'is_home': False,
        'additional_js': True,
    }
    return render(request, 'automation/pages/home.html', context)


def light(request):

    page = 'Luzes'
    context = {
        'banner': banner(),
        'tabs': subnav(),
        'content':  {
            'info': subnav_content(page),
        },
        'is_home': False,
        'additional_js': False,
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
