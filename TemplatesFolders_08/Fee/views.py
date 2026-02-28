from django.shortcuts import render

# Create your views here.
def fvone(request):
    fee={'fe':10300}
    return render(request, 'fee/feeone.html',fee)

def fvtwo(request):
    scholarship={'sp':26000}
    return render(request, 'fee/feetwo.html',scholarship)    