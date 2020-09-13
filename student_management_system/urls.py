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
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


