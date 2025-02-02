from django.urls import path
from .views import FaqListView
from django.http import HttpResponse

urlpatterns = [
    path('api/faqs/', FaqListView.as_view(), name='faq-list'),  
    path('', lambda request: HttpResponse("Welcome to the FAQ application!")),
]
