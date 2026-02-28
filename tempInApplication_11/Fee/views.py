from django.shortcuts import render

# Create your views here.
dic={
    'std1':{'fee':10222, 'semester':2},
    'std2':{'fee':20333, 'semester':5},
    'std3':{'fee':40000, 'semester':6}
}

def fee_view(request):
    return render(request, 'fee/feeone.html',dic)