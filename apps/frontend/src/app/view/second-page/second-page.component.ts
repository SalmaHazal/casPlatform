import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // Import RouterModule to enable routerLink
import { AuthNavbarComponent } from '../../layout/auth-navbar/auth-navbar.component';
import { FooterComponent } from '../../layout/footer/footer.component';

@Component({
  selector: 'app-second-page',
  standalone: true,
  imports: [
    RouterModule, // Add RouterModule here
    AuthNavbarComponent,
    FooterComponent
  ],
  templateUrl: './second-page.component.html',
  styleUrls: ['./second-page.component.css'] // Replace 'styleUrl' with 'styleUrls'
})
export class SecondPageComponent {
  showForm: boolean = false;

  // This function is called when the user clicks on "Find Sponsors" or "Sponsor Our Activities"
  onShowForm() {
    this.showForm = true;
  }
}
