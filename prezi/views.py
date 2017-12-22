from django.shortcuts import render

from prezi.models import Prezi

def prezi_list(request):
    return render(request, 'prezi/prezi_list.html', {'prezis': Prezi.objects.all()})
