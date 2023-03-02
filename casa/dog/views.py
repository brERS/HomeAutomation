from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('dog/pages/home.html')
    return HttpResponse(template.render())

def dog(request):
    template = loader.get_template('dog/pages/dog.html')
    return HttpResponse(template.render())


def agua(request):

    # Import RPi.GPIO module
    import RPi.GPIO as GPIO
    # Import module for delay
    from time import sleep

    # Disable message warnings
    GPIO.setwarnings(False)

    # Set pin specification mode choose BCM or BOARD
    GPIO.setmode(GPIO.BOARD)

    # Set GPIO port as an output
    GPIO.setup(18, GPIO.OUT)

    # Set GPIO port to False or True
    GPIO.output(18, False)

    # Progress bar
    for i in range(60):
        sleep(1)

    # Set GPIO port to False or True
    GPIO.output(18, True)

    return HttpResponse("Deu bom, baby dogs já tem água para beber!")
