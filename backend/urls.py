from django.contrib import admin
from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_data, name='index'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('update/<int:id>/', views.updatedata, name='update'),
]
