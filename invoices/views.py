from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt

from .handlers.webhook import webhook
    

@csrf_exempt
def webhook_handler(request: WSGIRequest) -> JsonResponse:
    
    if request.method == "POST":
        return webhook(request=request) 

    return JsonResponse({"message": "Method not allowed"}, status=405)
   