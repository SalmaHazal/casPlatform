import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthNavbarComponent } from '../../../layout/auth-navbar/auth-navbar.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, AuthNavbarComponent],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  // ...
}
