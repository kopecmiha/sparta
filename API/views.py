from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import User, Event, Times
import json
from datetime import datetime

def users(request):
    user_list = str(list(User.objects.all())).replace("'", '"')
    user_list = json.loads(user_list)
    return JsonResponse({"result": user_list})

def sparta(request):
    times_list = str(Times.objects.filter(id=1))
    return JsonResponse({"message": times_list})
def events(request):
    event_list = json.loads(str(list(Event.objects.all())).replace("'", '"'))
    for i in range(len(event_list)):
        idi = event_list[i]['id']
        times_list = json.loads(str(list(Times.objects.filter(event=idi))).replace("'", '"'))
        event_list[i].update({'times' : times_list})
    event_list = json.loads(str(event_list).replace("'", '"'))
    return JsonResponse({"result": event_list})

def times(request):
    times_list = str(list(Times.objects.all())).replace("'", '"')
    times_list = json.loads(times_list)
    return JsonResponse({"result": times_list})

@csrf_exempt
def write_event(request):
    if request.method == "POST":
        name = request.POST.get('name')
        r = Event(name = name)
        r.save()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def delete_event(request):
    if request.method == "POST":
        event_id = request.POST.get('id')
        Event.objects.filter(id=event_id).delete()
        Times.objects.filter(event=event_id).delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def update_event(request):
    if request.method == "POST":
        event_id = request.POST.get('id')
        dictionary = request.POST.dict()
        Event.objects.filter(id=event_id).update(**dictionary)
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def write_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        r = User(username = username, email = email)
        r.save()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def delete_user(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        User.objects.filter(id=user_id).delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def update_user(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        dictionary = request.POST.dict()
        User.objects.filter(id=user_id).update(**dictionary)
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def write_time(request):
    if request.method == "POST":
        time_start = request.POST.get('time_start')
        time_start = datetime.timestamp(datetime.strptime(time_start, "%d.%m.%Y %H:%M"))
        time_finish = request.POST.get('time_finish')
        time_finish = datetime.timestamp(datetime.strptime(time_finish, "%d.%m.%Y %H:%M"))
        event = request.POST.get('event_id')
        r = Times(time_start = time_start, time_finish = time_finish, event = event)
        r.save()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def delete_time(request):
    if request.method == "POST":
        time_id = request.POST.get('id')
        Times.objects.filter(id=time_id).delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def update_time(request):
    if request.method == "POST":
        time_id = request.POST.get('id')
        dictionary = request.POST.dict()
        Times.objects.filter(id=time_id).update(**dictionary)
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)