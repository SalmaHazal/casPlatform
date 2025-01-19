import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // Enables routerLink
import { AuthNavbarComponent } from '../../layout/auth-navbar/auth-navbar.component';
import { FooterComponent } from '../../layout/footer/footer.component';
import { EmailServiceService } from '../../email-service.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule

@Component({
  selector: 'app-second-page',
  standalone: true,
  imports: [
    RouterModule, // Add RouterModule for routing
    AuthNavbarComponent,
    FooterComponent,
    CommonModule,
    FormsModule, // Add FormsModule for ngModel support
  ],
  templateUrl: './second-page.component.html',
  styleUrls: ['./second-page.component.css'], // Correct property name is styleUrls
})
export class SecondPageComponent {
  showForm = false;
  formData = {
    userName: '',
    userEmail: '',
    userMessage: '',
  };
  constructor(private emailService: EmailServiceService) {}
  logMessage(message: string): void {
    console.log(message);
  }

  onSubmit() {
    this.emailService.sendEmail(this.formData);
  }

  // Function to display the form
  onShowForm() {
    this.showForm = true;
  }
}
