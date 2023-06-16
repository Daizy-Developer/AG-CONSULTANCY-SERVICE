from django.shortcuts import render ,HttpResponse
from web.models import *
from twilio.rest import Client

from django.conf import settings
from django.core.mail import send_mail


def index(request):

    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        # about = request.POST['about']
        Date_Time = request.POST['Date_Time']
        new_consult = Cosultation(Name=Name, Email=Email, Phone=Phone,Date_Time=Date_Time)
        new_consult.save()
        subject = 'Your Service Has Been Booked'
        message = f'Hi {Name}, Your Consulting Has Been Booked Kindly Join this Meeting At The Booking Time By Below Link '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [Email]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,"site/messagesent.html",{"text":message})
    project = Project.objects.all()
    return render(request,"site/index.html",{'project':project})



def services(request):
    if request.method=='POST':
        SR_NO = request.POST['sr_no']
        PASSWORD = request.POST['password']
        # print(USR_NAME ,PASSWORD)
        try:
            sr_no = Service_No.objects.get(id=SR_NO, password=PASSWORD)
            all_services = Service.objects.filter(service_no=sr_no)
            request.session['services_rendered'] = True
            return render(request,"site/allservice.html",{'data':all_services})
        except Service_No.DoesNotExist:
            print("error")
        if 'services_rendered' in request.session:
            all_services = Service.objects.filter(service_no=sr_no)
            return render(request, "site/allservice.html", {'data': all_services})
        
    return render(request,"site/service.html")


def Get_Quote(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        about = request.POST['about']
        Looking = request.POST['option']



        new_quotation = Quotation(Name=name, Email=email, Phone=phone,Looking=Looking,Budget=0)
        new_quotation.save()
        subject = 'Your Service Has Been Booked'
        message = f'Hi {name}, Your Consulting Has Been Booked Kindly Join this Meeting At The Booking Time By Below Link '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        return render(request, "site/messagesent.html",{"text":message})

    return render(request,"site/quote.html")
