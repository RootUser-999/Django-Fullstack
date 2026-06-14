from django.http import HttpResponse


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(' one time BrotherMiddleware initialized')
    
    def __call__(self,request):
        print('BrotherMiddleware before view')
        response= self.get_response(request)
        print('BrotherMiddleware after view')
        return response
    
class FatherMiddleware:
    def __init__ (self, get_response):
        self.get_response = get_response
        print(' one time FatherMiddleware initialized')

    def __call__(self,request):
        print('FatherMiddleware before view')
        # response=self.get_response(request)
        response =HttpResponse("Father Middleware Response")
        print('FatherMiddleware after view')
        return response

class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("mother middle ware one time initialization")

    def __call__(self, request):
        print("mother middle ware before view")
        response=self.get_response(request)
        print("mother after view")
        return response

