from django.shortcuts import render
from django.http import HttpResponse,FileResponse
import os
from django.http import FileResponse, HttpResponse

#this willa handle sem request         1. SEMESTER  FILTER  ===============
def sem(request):
    a=request.GET.get('sem')
    if(a==1):
        return render(request,'sem1_dashbord.html')
    if(a==2):
        return render(request,'sem2_dashbord.html')
    if(a==3):
        return render(request,'sem3_dashbord.html')
    if(a==4):
        return render(request,'sem4_dashbord.html')
    if(a==5):
        return render(request,'sem5_dashbord.html')
    if(a==6):
        return render(request,'sem6_dashbord.html')
    

    #==============handle subject request coming from different componrnts with each subject has unique id
def subject(request):
    a=request.GET.get('q')
    if a=='maths':
        return render(request,'maths.html')
    if a=='dstl':
        return render(request,'dstl.html')
    if a=='coa':
        return render(request,'coa.html')
    if a=='dsa':
        return render(request,'dsa.html')
    if a=='de':
        return render(request,'de.html')
    if a=='hv':
        return render(request,'hv.html')
    if a=='python':
        return render(request,'python.html')
    if a=='cyber':
        return render(request,'cyber.html')







def dashbord(request):
    return render(request,'sem3_dashbord.html')




#------------------------------------------notes--------------------------
def notes(request):  
    id=request.GET.get('q')
    filepath = os.path.join("media", "document.pdf")
    from django.http import FileResponse, HttpResponse

def notes(request):
    q = request.GET.get('q')  
    if q== "maths_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\maths.pdf", 'rb'),
                            content_type='application/pdf')
    if q== "python_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\python.pdf", 'rb'),
                            content_type='application/pdf')
    if q== "coa_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\coa.pdf", 'rb'),
                            content_type='application/pdf')
    if q== "dsa_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\dsa.pdf", 'rb'),
                            content_type='application/pdf')
    if q== "dstl_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\dstl.pdf", 'rb'),
                            content_type='application/pdf')
    if q== "cyber_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\cyber.pdf", 'rb'),
                            content_type='application/pdf')
    if q== "hv_notes":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\hv.pdf", 'rb'),
                            content_type='application/pdf')
              
def pyq():
    return 0



def dpp():
    


    

    


    

    if(id==1):   #===================python notes==================
     return FileResponse(open(r"C:\Users\Shivam\Downloads\book-list.pdf", 'rb'), content_type='application/pdf')
    
    
   

   
