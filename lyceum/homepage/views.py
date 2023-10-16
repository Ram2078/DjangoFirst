from django.http import HttpResponse


def index(request):
    return HttpResponse("Вы на домашней странице. Вы можете перейти на 'catalog/'"
                        " или 'about/'")