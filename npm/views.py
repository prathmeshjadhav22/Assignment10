from django.http import HttpResponse

def Index(request):
    return HttpResponse("this is home")