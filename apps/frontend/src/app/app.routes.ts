import { Route } from '@angular/router';
import { IndexComponent } from './view/index/index.component';
import { LoginComponent } from './view/auth/login/login.component';
import { SecondPageComponent } from './view/second-page/second-page.component';
import { SponsorsComponent } from './view/admin/sponsors/sponsors.component';

import { PageWithNavbarSidebarComponent } from './view/page-with-navbar-sidebar/page-with-navbar-sidebar.component';
import { SignUpComponent } from './view/auth/sign-up/sign-up.component';
import { DashboardComponent } from './view/admin/dashboard/dashboard.component';

export const appRoutes: Route[] = [
  // Route principale
  { path: '', component: IndexComponent },

  { path: 'second-page', component: SecondPageComponent },

  // Authentification
  { path: 'login', component: LoginComponent },
  { path: 'register', component: SignUpComponent },

  // Page avec navbar et sidebar
  {
    path: 'page-with-navbar-sidebar',
    component: PageWithNavbarSidebarComponent,
    children: [
      { path: 'dashboard', component: DashboardComponent },
      { path: 'sponsors', component: SponsorsComponent },
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' }, // Redirige vers "dashboard" par défaut
    ],
  },

  // Catch-all pour les routes inexistantes
  { path: '**', redirectTo: '' },
];


