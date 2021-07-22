from django.shortcuts import render

from ca.client.eye import TheEye
from ca.core.management.commands.process_events import Command


# dumb example of register/login
TheEye.wants_to_see(app='example', pwd='pass')


def index(request):
    # send a page view to the eye!
    TheEye().sees_page_interaction(request, name="pageview")
    return render(request, 'example/index.html', context={})


def chat(request):
    # send a page click to the eye!
    TheEye().sees_page_interaction(request, name="cta click")
    return render(request, 'example/index.html', context={})


def send(request):
    # send a form submit to the eye!
    TheEye().sees_form_interaction(request)
    return render(request, 'example/index.html', context={})


def process(request):
    Command().handle()
    return render(request, 'example/index.html', context={})
