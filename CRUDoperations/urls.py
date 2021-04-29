from django.urls import path

from CRUDoperations import views

urlpatterns = [
    path('',views.insertdata,name='insertData'),
    path('show',views.show,name='showData'),
    path('edit/<int:id>',views.edit,name='EditDetails'),
    path('delete/<int:id>',views.delete,name='deletingData')
]
