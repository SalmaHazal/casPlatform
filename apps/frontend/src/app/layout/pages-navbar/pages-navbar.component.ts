// auth-navbar.component.ts
import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-pages-navbar',
  standalone: true,
  imports: [
    CommonModule, 
    RouterModule, 
     // Ajoutez cette ligne
  ],
  templateUrl: './pages-navbar.component.html',
  styleUrls: []
})
export class PagesNavbarComponent {
  navbarOpen: boolean = false;
  dropdownPopoverShow: boolean = false; // État du menu déroulant

  setNavbarOpen() {
    this.navbarOpen = !this.navbarOpen;
  }

  toggleDropdown(event: Event): void {
    this.dropdownPopoverShow = !this.dropdownPopoverShow; // Inverse l'état du menu déroulant
    event.preventDefault(); // Empêche le comportement par défaut du lien
  }
}
