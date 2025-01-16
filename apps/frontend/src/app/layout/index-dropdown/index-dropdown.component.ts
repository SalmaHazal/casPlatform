import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-index-dropdown',
  standalone: true,
  imports: [CommonModule, RouterModule], // Ajoutez RouterModule ici
  templateUrl: './index-dropdown.component.html',

})
export class IndexDropdownComponent {
  dropdownPopoverShow = false;

  toggleDropdown(event: Event) {
    this.dropdownPopoverShow = !this.dropdownPopoverShow;
  }
}
