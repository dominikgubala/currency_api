from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status
from .views import CurrencyListView, CurrencyByDateView, FetchCurrencyView

class CurrencyURLsTestCase(TestCase):
    def test_currencies_list_url_resolves(self):
        url = '/api/currencies/'
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CurrencyListView)

    def test_currencies_fetch_url_resolves(self):
        url = '/api/currencies/fetch/'
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, FetchCurrencyView)

    def test_currency_by_date_url_resolves(self):
        url = '/api/currencies/2026-01-30/'
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CurrencyByDateView)

    def test_get_currencies_list(self):
        response = self.client.get('/api/currencies/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

    def test_get_currency_by_date(self):
        response = self.client.get('/api/currencies/2026-01-30/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])

    def test_fetch_currencies(self):
        response = self.client.post('/api/currencies/fetch/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED, status.HTTP_204_NO_CONTENT])

