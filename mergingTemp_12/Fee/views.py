from django.shortcuts import render

# Create your views here.

def fee_view(request):
    return render(request, 'fee/feeone.html')
