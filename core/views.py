from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.core.mail import send_mail
from . models import timetable, blog, event
from . forms import StudentRegisterForm as regform
from . message import student_content

from student_management_app.models import CustomUser, Staffs, Departments, Subjects, Students, SessionYearModel, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, LeaveReportStaff, Attendance, AttendanceReport
from student_management_app.forms import AddStudentForm, EditStudentForm
from datetime import date

today = date.today()


# Textual month, day and year	

# Create your views here.
def home(request):
    recent_news = blog.objects.all().order_by('-date_posted')[:8]
    event_data = event.objects.all()[:12]
    context = {
        'recent_news': recent_news,
        'event_data':event_data
    }
    return render(request, 'core/homepage-1.html', context)

def cruise(request):
    return render(request, 'core/default.html')

def Denied(request):
    return render(request, 'core/access-denied.html')


def about(request):
    return render(request, 'core/about-us.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def news_update(request):
    news = blog.objects.all().order_by('-date_posted')
    recent = blog.objects.all().order_by('date_posted')[:5]

    return render(request, 'core/blog.html',{'news':news, 'recent':recent})


def courses_department(request):
    return render(request, 'core/alumni-directory.html')

# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3",
# 		auth=(),
# 		data={"from": "Mailgun Sandbox <postmaster@samailgun.org>",
# 			"to": "Jeph Praise <jsnr300@gmail.com>",
# 			"subject": "Hello Jeph Praise",
# 			"text": "Congratulations Jeph Praise, you just sent an email with Mailgun!  You are truly awesome!"})

# send_simple_message()

def apply(request):
    form = regform(request.POST)
    sent = False
    if request.method == 'POST':
    # Form was submitted
        if form.is_valid():
    # Form fields passed validation
            d2 = today.strftime("%B %d, %Y")
            year = today.strftime("%Y")
            name = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            first_language = form.cleaned_data.get('first_language')
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            course_of_study = form.cleaned_data.get('course_of_study')
            content =    f"""
African University of Benin

Hi there {name} {lastname} thanks for taking the time to fill the form, to complete your application process please fill the final form, to help us know more about you,

https://docs.google.com/forms/d/e/1FAIpQLSemefapPz2uLXe8TQy2Jj16YFqhK59mkwO-Gt8TpWC-fVor3g/viewform, 


please we require you to fill this form with correct information.

we hope to see you Soon, Cheers!

Akujuobi Praise
admissions coordinator | African University Of Benin
{d2}
source: https://aubcotonou.org

©{year} ❤️ African University of Benin
    """
            school_content = f"""
{name} {lastname} filled the Applocation form.
first language: {first_language}
country: {country}
state: {state}  
selected course: {course_of_study}

AUB Application Form
admissions Process | African University of Benin
{d2}
source: https://aubcotonou.org

©{year} ❤️ African University of Benin
            """
            send_mail(f"African University of Benin, Application process", content, 'contact_email',[email])
            send_mail(f"{name} {lastname} Submitted the Form",  school_content, 'contact_email',['africanuniversityofbenin2016@gmail.com'])

            messages.success(request,f"Congratulations!! {name} {lastname} You Have sucessfully completed the first stage of you Application into our University.") 
            return redirect('success')
    else:
        form = regform()
        messages.success(request,f"Email was not sucesfully sent!") 
    return render(request, 'core/form.html', {'form':form})

def Timetable(request):
    departments = Departments.objects.all()
    item = timetable.objects.all()
    context = {
        "departments":departments,
        "item":item
    }
    print(item)
    return render(request, 'core/timetable.html', context)


def calendar(request):
    data = event.objects.all()
    return render(request, 'core/programs-events.html', {"data":data})

def tuition(request):
    return render(request, 'core/pricing-table.html')

def lecturers(request):
    return render(request, 'core/our-lecturers.html')

def successView(request):
    return render(request, 'core/success.html')