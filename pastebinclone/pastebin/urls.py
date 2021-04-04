from django.urls import path
from . import views

app_name = 'pastebin'
urlpatterns = [
    path('', views.createPaste, name='createPaste'),
    path('pastebins', views.pastebins, name='pastebins'),
    path('<int:pastebin_id>/', views.pastebinDetails, name="pastebinDetails")
]