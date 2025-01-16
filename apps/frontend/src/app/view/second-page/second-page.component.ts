import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // Importez RouterModule pour activer routerLink
import { AuthNavbarComponent } from '../../layout/auth-navbar/auth-navbar.component';
import { FooterComponent } from '../../layout/footer/footer.component';

@Component({
  selector: 'app-second-page',
  standalone: true,
  imports: [
    RouterModule, // Ajoutez RouterModule ici
    AuthNavbarComponent,
    FooterComponent
  ],
  templateUrl: './second-page.component.html',
  styleUrls: ['./second-page.component.css'] // Remplacez 'styleUrl' par 'styleUrls'
})
export class SecondPageComponent {}

