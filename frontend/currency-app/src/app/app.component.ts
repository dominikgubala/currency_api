import { Component } from '@angular/core';
import { CurrencyTableComponent } from './components/currency-table/currency-table.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CurrencyTableComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'currency-app';
}
