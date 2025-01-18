import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SidebarComponent } from '../../layout/sidebar/sidebar.component';

@Component({
  selector: 'app-page-with-navbar-sidebar',
  standalone: true,
  imports: [SidebarComponent, RouterOutlet],
  templateUrl: './page-with-navbar-sidebar.component.html',
  styleUrls: ['./page-with-navbar-sidebar.component.css']
})
export class PageWithNavbarSidebarComponent {
  // Votre logique ici
}
