import { Component, OnInit, inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FaIconLibrary, FaConfig, FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { fontAwesomeIcons } from './shared/font-awesome-icons';

@Component({
  imports: [RouterModule, FontAwesomeModule, FontAwesomeModule],
  selector: 'cas-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent implements OnInit {
  private faIconLibrary: FaIconLibrary = inject(FaIconLibrary); // Explicit type annotation
  private faConfig: FaConfig = inject(FaConfig); // Explicit type annotation

  ngOnInit(): void {
      this.initFontAwesome();
    }

  private initFontAwesome() {
      this.faConfig.defaultPrefix = 'far';
      this.faIconLibrary.addIcons(...fontAwesomeIcons);
    }
}
