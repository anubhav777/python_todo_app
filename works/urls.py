from django.urls import path
from .views import Form_display,form_delete,edit_form

app_name='works'
urlpatterns=[
    path('form/',Form_display,name='formdisplay'),
    path('delete/<int:id>',form_delete,name='detail'),
    path('editform/<int:id>',edit_form,name='editform')
]