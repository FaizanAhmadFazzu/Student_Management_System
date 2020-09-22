from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from student_management_app import views, HodViews
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo', views.showDemoPage),
    path('', views.showLoginPage, name="show_login"),
    path('doLogin', views.doLogin, name="do_login"),
    path('get_user_details', views.GetUserDetails, name="get_user_details"),
    path('logout_user', views.logout_user, name="logout"),
    path('admin_home', HodViews.admin_home, name="admin_home"),
    path('add_staff', HodViews.add_staff, name="add_staff"),
    path('add_staff_save', HodViews.add_staff_save, name="add_staff_save"),
    path('add_course', HodViews.add_course, name="add_course"),
    path('add_course_save', HodViews.add_course_save, name="add_course_save"),
    path('add_student', HodViews.add_student, name="add_student"),
    path('add_student_save', HodViews.add_student_save, name="add_student_save"),
    path('add_subject', HodViews.add_subject, name="add_subject"),
    path('add_subject_save', HodViews.add_subject_save, name="add_subject_save"),
    path('manage_staff', HodViews.manage_staff, name="manage_staff"),
    path('manage_student', HodViews.manage_student, name="manage_student"),
    path('manage_subject', HodViews.manage_subject, name="manage_subject"),
    path('manage_course', HodViews.manage_course, name="manage_course"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


