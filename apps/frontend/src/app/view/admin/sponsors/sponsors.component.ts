import { Component } from '@angular/core';
import { CardSettingsComponent } from '../../../layout/card-settings/card-settings.component';

@Component({
  selector: 'app-sponsors',
  standalone: true,
  imports : [CardSettingsComponent],
  templateUrl: './sponsors.component.html',
  styleUrls: ['./sponsors.component.css'],
})
export class SponsorsComponent {
  // Liste des sponsors mockée
  
}
