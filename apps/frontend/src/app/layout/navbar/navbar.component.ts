import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FontAwesomeModule, FaIconLibrary, FaConfig } from '@fortawesome/angular-fontawesome';
import { fontAwesomeIcons } from '../../shared/font-awesome-icons';
import { IndexDropdownComponent } from '../index-dropdown/index-dropdown.component';
@Component({
  selector: 'app-navbar',
  imports: [CommonModule, RouterLink, FontAwesomeModule, IndexDropdownComponent],
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  private faIconLibrary: FaIconLibrary = inject(FaIconLibrary);
  private faConfig: FaConfig = inject(FaConfig);

  ngOnInit(): void {
    this.initFontAwesome();
  }

  private initFontAwesome() {
    this.faConfig.defaultPrefix = 'fas';
    this.faIconLibrary.addIcons(...fontAwesomeIcons); 
  }
  navbarOpen = false;

  // Méthode pour basculer l'état de navbarOpen
  setNavbarOpen() {
    this.navbarOpen = !this.navbarOpen;
  }
  
}
