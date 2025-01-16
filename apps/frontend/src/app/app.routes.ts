import { Route } from '@angular/router';
import { IndexComponent } from './view/index/index.component';
import { LoginComponent } from './view/auth/login/login.component';
import { SecondPageComponent } from './view/second-page/second-page.component';

export const appRoutes: Route[] = [
  {
    path: '', // Route par défaut
    component: IndexComponent,
  },
  {
    path: 'login', // Route pour la page de connexion
    component: LoginComponent,
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

