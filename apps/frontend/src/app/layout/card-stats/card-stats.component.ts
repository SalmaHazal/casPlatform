import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-card-stats',
  standalone: true,
  imports: [CommonModule], // Import CommonModule ici
  templateUrl: './card-stats.component.html',
  styleUrls: ['./card-stats.component.css'],
})
export class CardStatsComponent {
  @Input() statSubtitle: string = '';
  @Input() statTitle: string = '';
  @Input() statArrow: 'up' | 'down' = 'up';
  @Input() statPercent: number = 0;
  @Input() statPercentColor: string = '';
  @Input() statIconName: string = '';
  @Input() statIconColor: string = '';
  @Input() statDescription: string = '';
}

