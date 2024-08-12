from django.shortcuts import render

def handler500(request):
    response = render(request, 'handler500.html')
    response.status_code = 500
    return response