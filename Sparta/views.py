from django.http import HttpResponse
from django.http import JsonResponse


def sparta(request):
    return JsonResponse({"message":"Hello Sparta"})