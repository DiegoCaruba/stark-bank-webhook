import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Invoice
    

@csrf_exempt
def webhook(request):

    print(f"WEBHOOK --> {type(request)}: {request} ~ {request.method}")
    if request.method == "POST":
        data = json.loads(request.body)
        invoice_id = data.get("id")
        invoice_status = data.get("status")

        try:
            invoice = Invoice.objects.get(id=invoice_id)
            invoice.status = invoice_status
            invoice.save()

            return JsonResponse({"message": "Invoice received successfully"}, status=200)
        
        except Invoice.DoesNotExist:
            return JsonResponse({"message": "Invoice not found"}, status=404)

    return JsonResponse({"message": "Method not allowed"}, status=405)

"""
@csrf_exempt
def webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        invoice_id = data.get("id")
        status = data.get("status")

        try:
            invoice = Invoice.objects.get(id=invoice_id)
            invoice.status = status
            invoice.save()
            return JsonResponse({"message": "Webhook recebido com sucesso"}, status=200)
        except Invoice.DoesNotExist:
            return JsonResponse({"error": "Invoice não encontrada"}, status=404)

    return JsonResponse({"error": "Método não permitido"}, status=405)


"""