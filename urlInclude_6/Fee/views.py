from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fee_view(request):
    return HttpResponse("Pay Your Dues")
def fee_voucher(request):
    return HttpResponse("<h2 strong color:blue>Link<h3>")