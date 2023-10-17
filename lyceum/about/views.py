from django.http import HttpResponse


def index(request):
    return HttpResponse("Вы на странице 'О себе'.")
