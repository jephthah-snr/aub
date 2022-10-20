from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('access-denied/', views.Denied, name="denied"),
    path('aub/about/', views.about, name="about"),
    path('aub/gallery/', views.gallery, name="gallery"),
    path('aub/news/', views.news_update, name="news"),
    path('aub/courses&departments/', views.courses_department, name="courses"),
    path('aub/apply/', views.apply, name="apply"),
    path('aub/timetable/', views.Timetable, name="timetable"),
    path('aub/calendar/', views.calendar, name="calendar"),
    path('aub/tuition', views.tuition, name = "tuition"),
    path('aub/lecturers/', views.lecturers, name="lecturers"),
    path('aub/apply/success', views.successView, name="success"),
]




# def gallrey(request):
#     return render(request, 'core/gallery.html')

# def news_update(request):
#     return render(request, 'core/blog.html')


# def courses_department(request):
#     return render(request, 'core/alumni-directory.html')