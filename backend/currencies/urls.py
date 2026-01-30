from django.urls import path
from .views import CurrencyListView, CurrencyByDateView, FetchCurrencyView

urlpatterns = [
    path('currencies/', CurrencyListView.as_view()),
    path('currencies/fetch/', FetchCurrencyView.as_view()),
    path('currencies/<str:date_str>/', CurrencyByDateView.as_view()),
]
