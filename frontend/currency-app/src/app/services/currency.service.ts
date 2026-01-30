import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface CurrencyRate {
  currency: string;
  rate: number;
  date: string;
}

@Injectable({
  providedIn: 'root'
})
export class CurrencyService {
  private apiUrl = 'http://localhost:8000/api/currencies';

  constructor(private http: HttpClient) {}

  fetchCurrencies(): Observable<any> {
    return this.http.post(`${this.apiUrl}/fetch/`, {});
  }

  getCurrencies(): Observable<CurrencyRate[]> {
    return this.http.get<CurrencyRate[]>(this.apiUrl + '/');
  }

  getCurrenciesByDate(date: string): Observable<CurrencyRate[]> {
    return this.http.get<CurrencyRate[]>(`${this.apiUrl}/${date}/`);
  }
}
