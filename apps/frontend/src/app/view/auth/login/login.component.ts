import { Component } from '@angular/core';
import { RouterLink, Router } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AuthNavbarComponent } from '../../../layout/auth-navbar/auth-navbar.component';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    RouterLink,
    AuthNavbarComponent,
    CommonModule,
    FormsModule,
    HttpClientModule,
  ],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  user = {
    email: '',
    password: '',
  };

  constructor(private http: HttpClient, private router: Router) {}

  onLogin(form: any) {
    if (form.valid) {
      this.http
        .post('http://localhost:8090/api/v1/user/login', this.user, { responseType: 'text' })
        .subscribe({
          next: (response) => {
            console.log('User signed in successfully', response);
            this.router.navigate(['/second-page']);
          },
          error: (error) => console.error('Error signing in user', error),
          complete: () => console.log('login request completed'),
        });
    }
  }
}
