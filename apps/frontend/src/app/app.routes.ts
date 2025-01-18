import { Route } from '@angular/router';
import { IndexComponent } from './view/index/index.component';
import { LoginComponent } from './view/auth/login/login.component';
import { SecondPageComponent } from './view/second-page/second-page.component';
import { SignUpComponent } from './view/auth/sign-up/sign-up.component';

export const appRoutes: Route[] = [
  {
    path: '',
    component: IndexComponent,
  },
  {
    path: 'login', // Route pour la page de connexion
    component: LoginComponent,
  },
  {
    path: 'register',
    component: SignUpComponent,
  },
  {
    path: 'second-page', // Route pour la page de connexion
    component: SecondPageComponent,
  },
  {
    path: '**', // Redirection pour toutes les routes inexistantes
    redirectTo: '',
  },
];

