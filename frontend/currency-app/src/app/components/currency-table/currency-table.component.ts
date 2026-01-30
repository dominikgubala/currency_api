import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CurrencyService, CurrencyRate } from '../../services/currency.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-currency-table',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './currency-table.component.html',
  styleUrls: ['./currency-table.component.scss']
})
export class CurrencyTableComponent implements OnInit {
  currencies: CurrencyRate[] = [];
  selectedDate: string = '';

  constructor(private currencyService: CurrencyService) {}

  ngOnInit(): void {
    this.loadCurrencies();
  }

  loadCurrencies() {
    this.currencyService.getCurrencies().subscribe(data => this.currencies = data);
  }

  fetchData() {
    this.currencyService.fetchCurrencies().subscribe(() => this.loadCurrencies());
  }

  loadByDate() {
    if (this.selectedDate) {
      this.currencyService.getCurrenciesByDate(this.selectedDate).subscribe(data => {
        this.currencies = data;
      });
    }
  }
}
