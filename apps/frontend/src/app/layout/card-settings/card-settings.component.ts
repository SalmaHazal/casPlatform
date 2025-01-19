import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-card-settings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './card-settings.component.html',
  styleUrl: './card-settings.component.css'
})
export class CardSettingsComponent {
  sponsors = [
    { name: 'Company Name', sector: 'Technology', address: '1234 Example St.' },
    { name: 'Another Company', sector: 'Marketing', address: '5678 Sample Rd.' },
  ];

  contactSponsor(sponsor: any): void {
    console.log('Contacting sponsor:', sponsor);
    // Ajoutez ici la logique pour contacter le sponsor
  }

}
