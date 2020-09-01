from django.http import HttpResponse
import datetime

def hola(request):
    return HttpResponse("hola")
    
def hora(request):
    return HttpResponse(datetime.datetime.now())
