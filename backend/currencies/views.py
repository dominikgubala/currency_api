from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CurrencyRate
from .serializers import CurrencyRateSerializer
import requests
from datetime import date, timedelta

class CurrencyListView(APIView):
    def get(self, request):
        rates = CurrencyRate.objects.all()
        serializer = CurrencyRateSerializer(rates, many=True)
        return Response(serializer.data)

class CurrencyByDateView(APIView):
    def get(self, request, date_str):
        rates = CurrencyRate.objects.filter(date=date_str)
        serializer = CurrencyRateSerializer(rates, many=True)
        return Response(serializer.data)

class FetchCurrencyView(APIView):
    def post(self, request):
        # Pobranie tabeli z requestu (domyślnie 'A')
        table = request.data.get('table', 'A')
        
        # Obliczenie dat
        end_date = date.today()
        start_date = end_date - timedelta(days=30)
        
        # Formatowanie dat w ISO 8601
        start_date_str = start_date.isoformat()  # YYYY-MM-DD
        end_date_str = end_date.isoformat()      # YYYY-MM-DD
        
        # URL z zakresem dat
        url = f"https://api.nbp.pl/api/exchangerates/tables/{table}/{start_date_str}/{end_date_str}/?format=json"
        response = requests.get(url)
        
        if response.status_code == 200:
            tables = response.json()
            for data in tables:
                rates = data['rates']
                effective_date = data['effectiveDate']
                for r in rates:
                    CurrencyRate.objects.get_or_create(
                        currency=r['code'],
                        date=effective_date,
                        defaults={'rate': r['mid']}
                    )
            return Response({"message": f"Data fetched for table {table}."})
        
        return Response({"error": "NBP API error."}, status=500)
