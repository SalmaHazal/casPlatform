import { Component } from '@angular/core';
import { CardBarChartComponent } from '../../../layout/card-bar-chart/card-bar-chart.component';
import { CardLineChartComponent } from '../../../layout/card-line-chart/card-line-chart.component';
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CardBarChartComponent, CardLineChartComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {

}
