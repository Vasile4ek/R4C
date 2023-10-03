import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

from .models import Robot


# @csrf_exempt
def robots_api(request):
    """Принимает json вида {"model":"R2","version":"D2","created":"2022-12-31 23:59:59"} и кладёт в базу"""
    # if request.method != "POST":
    #     return HttpResponseBadRequest(f"Unsupported method {request.method}")

    try:
        data = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse(dict(success=False, error="Invalid Json"))

    model = data.get("model", None)
    version = data.get("version", None)
    created = data.get("created", None)

    robot = Robot(serial=f"{model}-{version}", model=model, version=version, created=created)

    try:
        robot.full_clean(exclude=["serial"])
        robot.save()
        return JsonResponse(dict(success=True, robot=dict(model=model, version=version, created=created)))
    except ValidationError as e:
        return JsonResponse(dict(success=False, error=e.message_dict))
