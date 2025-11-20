from django.shortcuts import render

def error404(request, exception): return render(request, 'errors/404.html', {"pageURLs": {"home": "/"}}, status=404) 

def error500(request): return render(request, 'errors/500.html', {"pageURLs": {"home": "/"}}, status=500) 
