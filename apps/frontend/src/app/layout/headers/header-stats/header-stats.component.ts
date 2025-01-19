import { Component } from '@angular/core';
import { CardStatsComponent } from '../../card-stats/card-stats.component';
import { CommonModule } from '@angular/common'

@Component({
  selector: 'app-header-stats',
  standalone: true,
  imports: [CardStatsComponent, CommonModule], // Ajout du composant à la liste des imports
  templateUrl: './header-stats.component.html',
  styleUrls: ['./header-stats.component.css'],
})
export class HeaderStatsComponent {}
