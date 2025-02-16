import json

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt

from ..models import Invoice
    

@csrf_exempt
def webhook(request: WSGIRequest) -> JsonResponse:
    
    if request.method == "POST":
        data: dict = json.loads(request.body)
        invoice_id: int = data.get("id")
        invoice_status: str = data.get("status")
        print(f" -->> WEBHOOK DATA -->> {data}")

        try:
            invoice = Invoice.objects.get(id=invoice_id)
            print(type(invoice), invoice)
            invoice.status = invoice_status
            invoice.save()

            return JsonResponse({"message": "Invoice received successfully"}, status=200)
        
        except Invoice.DoesNotExist:
            return JsonResponse({"message": "Invoice not found"}, status=404)
