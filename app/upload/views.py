from django.shortcuts import render

# Create your views here.

def upload_view(request):
    template_name = "upload.html"
    context = {
        "title" : "Upload"
    }
    return render(request, template_name, context)