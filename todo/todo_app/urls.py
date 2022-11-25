"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('admin/', admin.site.urls),
    path('View_All_List_Of_Task',views.View_All_List_Of_Task,name = 'View All List Of Task'),
    path('Add_Task',views.Add_Task,name = 'Add Task'),
    path('Delete_Task',views.Delete_Task,name = 'Delete Task'),
    path('Remove_Task/<int:item_id>',views.Delete_Task,name = 'Delete Task'),
    path('List_Completed_Task',views.List_Completed_Task,name = 'List Of Completed Task'),
    path('List_Pending_Task',views.List_Pending_Task,name = 'List Of pending Task'),
    path('Mark_as_completed_task',views.Mark_as_completed_task,name = 'Mark As Completed Task'),
]
