
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
  path('',views.blogs,name='blogs'),
  path('delete_blog/<id>/',views.delete_blog,name="delete"),
  path('update_blog/<id>/',views.update_blog,name="update"),
  path('login',views.login_page,name='login'),
  path('logout',views.logout_page,name='logout'),
  path('register',views.register_page,name='register')
 ]
