import { Route } from '@angular/router';
import { IndexComponent } from './view/index/index.component';
import { LoginComponent } from './view/auth/login/login.component';
import { SecondPageComponent } from './view/second-page/second-page.component';
import { PageWithNavbarSidebarComponent } from './view/page-with-navbar-sidebar/page-with-navbar-sidebar.component';
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
    path: 'page-with-navbar-sidebar', // Route pour la page de connexion
    component: PageWithNavbarSidebarComponent,
  },
  {
    path: '**', // Redirection pour toutes les routes inexistantes
    redirectTo: '',
  },
];

