from django.http import HttpResponse


class MyMiddleware:
    def __init__(self,get_response):
        self.get_response =get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
        
    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     print("Process view called")
    #     return None
    
    def process_exception(self,request,exception):
        return HttpResponse("Exception handled in middleware: "+str(exception))