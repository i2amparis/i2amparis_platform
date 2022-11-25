# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib
from urllib import request
from urllib import parse

from django.shortcuts import render

from django.shortcuts import render

from .forms import FeedbackForm
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

import json

def feedback_form(request):
    # if request.user.is_authenticated():
    #     username = request.user.username
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                # This can be used to send an email to inform us about the newly submitted feedback.
                action = form.cleaned_data['service']
                details = form.cleaned_data['details']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                rating = str(form.cleaned_data['rating'])
                email_text = 'User: "' + str(username) + '" submitted his/her feedback on I2AM Paris Platform, regarding: "' + str(
                    action) + '".\nComment: "' + str(details) + '"\nRating: ' + str(rating) + '/5 stars. \nE-mail:' + email
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'

                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req = urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                ''' End reCAPTCHA validation '''
                if result['success']:
                    try:
                        form.save()
                        messages.success(request, 'New comment added with success!')
                        print('New comment added with success!')
                    except:
                        messages.error(request, 'The evaluation could not be stored!')
                        print('The evaluation could not be stored!')
                        return JsonResponse({'status': 'NOT_OK_FORM_NOT_SAVED'})
                    try:
                        send_mail(str(username) + "'s Feedback on I2AM Paris Platform", email_text, 'noreply@epu.ntua.gr',
                                  ['iam@paris-reinforce.eu', 'paris.reinforce@gmail.com'],
                                  fail_silently=False)
                    except:
                        messages.error(request, 'The evaluation was stored but email to paris-reinforce could not be sent! SMTP server credentials may be wrong!')
                        print('The evaluation was stored but email to paris-reinforce could not be sent! SMTP server credentials may be wrong!')
                    return JsonResponse({'status': 'OK'})

                else:
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                    print('Invalid reCAPTCHA. Please try again.')
                    return JsonResponse({'status': 'NOT_OK_INVALID_CAPTCHA'})

        else:
            form = FeedbackForm()
        return render(request, 'feedback_form/feedback_form.html', {'form': form})
    # else:
    #     raise PermissionDenied