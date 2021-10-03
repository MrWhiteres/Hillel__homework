import random
import string

from django import forms
from django.shortcuts import render


def get_random_str(length, specials, digits):
    error = None
    try:
        length = int(length)
    except ValueError:
        return None, 'Length should be int'
    if 1 > length or length > 100:
        return None, 'Length should be 1~100'
    if digits not in (None, '1'):
        return None, 'Digits Should be 0 or 1'
    if specials not in (None, '1'):
        return None, 'Specials Should be 0 or 1'

    ran_choi = string.ascii_letters
    if specials:
        ran_choi += string.punctuation
    if digits:
        ran_choi += string.digits

    result = ''
    if length and not error:
        result = ''.join(random.choices(ran_choi, k=length))

    return result, None


def random_string(request):
    length = forms.CharField(widget=forms.NumberInput(attrs={'length': 'length'}))
    specials = forms.CheckboxInput()
    digits = forms.CheckboxInput()

    result, error = get_random_str(length, specials, digits)
    if error is None:
        error = ''

    date = {'result': result, 'error': error}
    return render(request, 'random.html', context=date)