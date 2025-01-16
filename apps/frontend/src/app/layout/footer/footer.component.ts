import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FontAwesomeModule, FaIconLibrary, FaConfig } from '@fortawesome/angular-fontawesome';
import { fontAwesomeIcons } from '../../shared/font-awesome-icons'; // Adjust the path if needed

@Component({
  selector: 'app-footer',
  imports: [CommonModule, FontAwesomeModule], // Add FontAwesomeModule
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss'], // Fix typo: styleUrl -> styleUrls
})
export class FooterComponent implements OnInit {
  private faIconLibrary: FaIconLibrary = inject(FaIconLibrary); // Inject FaIconLibrary
  private faConfig: FaConfig = inject(FaConfig); // Inject FaConfig

  ngOnInit(): void {
    this.initFontAwesome(); // Initialize FontAwesome icons
  }

  private initFontAwesome() {
    this.faConfig.defaultPrefix = 'fas'; // Set default prefix for solid icons
    this.faIconLibrary.addIcons(...fontAwesomeIcons); // Register icons from fontAwesomeIcons array
  }
  date: number = new Date().getFullYear();
}
