import { Component } from '@angular/core';
import {Router } from '@angular/router';
import { AuthNavbarComponent } from '../../../layout/auth-navbar/auth-navbar.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [
    AuthNavbarComponent,
    CommonModule,
    FormsModule,
    HttpClientModule,
  ],
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css'],
})
export class SignUpComponent {
  user = {
    userName: '',
    email: '',
    password: '',
    cell: '',
  };

  constructor(private http: HttpClient, private router: Router) {}

  onRegister(form: any) {
    if (form.valid) {
      this.http
        .post('http://localhost:8090/api/v1/user/register', this.user, { responseType: 'text' })
        .subscribe({
          next: (response) => {
            console.log('User registered successfully', response);
            this.router.navigate(['/login']);
          },
          error: (error) => console.error('Error registering user', error),
          complete: () => console.log('Registration request completed'),
        });
    }
  }
  
}
