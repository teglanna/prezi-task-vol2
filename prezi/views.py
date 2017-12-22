from django.shortcuts import render

def prezi_list(request):
    return render(request, 'prezi/prezi_list.html')
