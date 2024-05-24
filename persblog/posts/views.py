from django.http import HttpResponse

def index(request):
    return HttpResponse('Say Hi! to the Home...')
def home(request):
    return HttpResponse('welcome to persblog')
