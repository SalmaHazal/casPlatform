import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthNavbarComponent } from '../../../layout/auth-navbar/auth-navbar.component';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [RouterLink, AuthNavbarComponent],
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class LoginComponent {
  // ...
}
