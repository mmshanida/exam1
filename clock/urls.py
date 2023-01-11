from django.urls import path
from . import views
app_name='clock'
urlpatterns=[
    path('display',views.clock_display,name='display'),
]