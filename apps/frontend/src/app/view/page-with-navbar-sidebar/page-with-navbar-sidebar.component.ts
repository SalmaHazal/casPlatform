import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SidebarComponent } from '../../layout/sidebar/sidebar.component';
import { PagesNavbarComponent } from '../../layout/pages-navbar/pages-navbar.component';
import { HeaderStatsComponent } from '../../layout/headers/header-stats/header-stats.component';
@Component({
  selector: 'app-page-with-navbar-sidebar',
  standalone: true,
  imports: [SidebarComponent, RouterOutlet, PagesNavbarComponent, HeaderStatsComponent],
  templateUrl: './page-with-navbar-sidebar.component.html',
  styleUrls: ['./page-with-navbar-sidebar.component.css']
})
export class PageWithNavbarSidebarComponent {
  // Votre logique ici
}
