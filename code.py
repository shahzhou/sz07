from django.http import HttpResponse
def index(request):
    return HttpResponse('index')
def goods(request):
    return HttpResponse('goodds')

