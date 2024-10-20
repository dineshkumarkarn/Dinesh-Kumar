from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import UploadFileForm
from .utils import handle_uploaded_file
from .utils import  generate_summary_excel
from django.template import loader

# def nama(request):
#     # print("hello")
#     # template = loader.get_template('upload.html')
#     # return HttpResponse(template.render())
#     if request.method == 'POST':
#         summary = request.FILES['file']
#         create(summary)
#     return render(request,'Upload.html')
    
#     # else:
#     #     form = UploadFileForm(request.POST, request.FILES)
        
        
#     # return render(request,'Upload.html', {'form': form})

def create(file_path):
    df=pd.read_excel(file_path)  
    print(df.values)  


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary= request.FILES['file']
            create(summary)
            summary = handle_uploaded_file(request.FILES['file'])
            
            request.session['summary'] = summary
            
            return render(request, 'summary.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def export_summary(request):
    summary = request.session.get('summary')
    if summary:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=summary.xlsx'
        generate_summary_excel(summary, response)
        return response
    return HttpResponse("No summary available for export.")
