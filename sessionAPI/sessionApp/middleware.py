from django.shortcuts import HttpResponse


class CustomMiddleWare:

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("before performing operations on request")
        # perform operations and return request to next middleware or view
        response=self.get_response(request)
        print("response is going to the next middleware or view")
        return response
    

class ExceptionHandling:

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    # if exception occurs this method gets invoked

    def process_exception(self,request,exception):
        # returning friendly message so that he dont get panicked
        return HttpResponse("<h1>we are currently facing some issues come back later</h1>")
    

    """
    WE HAVE 
    ->PROCESS_VIEW AND 
    ->PROCESS_TEMPLATE_RESPONSE METHODS 
    TO PROCESS THE REQUESTS AND RESPONSES OF VIEWS AND TEMPLATES RENDERING
    """


    

