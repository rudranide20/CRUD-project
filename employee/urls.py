from django.urls import path
from . import views

urlpatterns = [
    path('emp',views.emp,name="emp"),
    path('',views.show,name="show" ),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.deletedata,name="delete"),
]