from random import choices
from django.db import models
from student_management_app.models import Subjects, CustomUser
from django.utils import timezone
# Create your models here.


class timetable(models.Model):
    days = [
        ('monday','monday'),
        ('tuesday','tuesday'),
        ('wednesday','wednesday'),
        ('thursday','thursday'),
        ('friday','friday')
    ]

    time = models.TimeField()
    course = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    day = models.CharField(max_length=30, choices = days, default='Full-time') 



class blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    article = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class event(models.Model):

    event_type = [
        ('event','event'),
        ('activity','activity'),
        ('reminder','reminder'),
        ('other','other'),
    ]

    title = models.CharField(max_length=50)
    event_location = models.CharField(max_length=50)        
    date_posted = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(default=None, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(default=None, null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    article = models.TextField()
    type_of = models.CharField(max_length=30, choices = event_type, default='event') 

    def __str__(self):
        return self.title


class register(models.Model):
    courses = [
        ('mass communication','mass communication'),
        ('computer science','computer science'),
        ('international relations','international relations'),
        ('business administration','business administration'),
        ('economics','economics'), 
    ]

    language = [
        ('english', 'english'),
        ('french','french'),
        ('other','other')  
    ]

    States = [
        ('Abia','Abia'),
        ('Adamawa','Adamawa'),
        ('Akwa Ibom','Akwa Ibom'),
        ('Anambra','Anambra'),
        ('Bauchi','Bauchi'),
        ('Bayelsa','Bayelsa'),
        ('Benue','Benue'),
        ('Borno','Borno'),
        ('Cross River','Cross River'),
        ('Delta','Delta'),
        ('Ebonyi','Ebonyi'),
        ('Edo','Edo'),
        ('Ekiti','Ekiti'),
        ('Enugu','Enugu'),
        ('Gombe','Gombe'),
        ('Imo','Imo'),
        ('Jigawa','Jigawa'),
        ('Kaduna','Kaduna'),
        ('Kano','Kano'),
        ('Katsina','Katsina'),
        ('Kebbi','Kebbi'),
        ('Kogi','Kogi'),
        ('Kogi','Kogi'),
        ('Lagos','Lagos'),
        ('Nasarawa','Nasarawa'),
        ('Niger','Niger'),
        ('Ogun','Ogun'),
        ('Ondo','Ondo'),
        ('Osun','Osun'),
        ('Oyo','Oyo'),
        ('Plateau','Plateau'),
        ('Rivers','Rivers'),
        ('Sokoto','Sokoto'),
        ('Taraba','Taraba'),
        ('Yobe','Yobe'),
        ('Zamfara','Zamfara'),
        ('FCT	Abuja','FCT	Abuja'),
        ('Not Nigerian', 'Not Nigerian')
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    # passport_photograph = models.FileField()
    phone_number = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    first_language = models.CharField(max_length=30, choices = language)
    state = models.CharField(max_length=30, choices = States)
    course_of_study = models.CharField(max_length=30, choices = courses)
    # Wassce_Waec = models.FileField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"