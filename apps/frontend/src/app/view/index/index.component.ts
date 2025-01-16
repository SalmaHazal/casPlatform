import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router'; // Inclure RouterModule uniquement si nécessaire
import { FooterComponent } from '../../layout/footer/footer.component';
import { NavbarComponent } from '../../layout/navbar/navbar.component';

@Component({
  selector: 'app-index',
  standalone: true,
  imports: [
    RouterModule,
    NavbarComponent,
     FooterComponent// Assurez-vous que c'est utilisé dans le fichier HTML
  ],
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css'],
})
export class IndexComponent implements OnInit {
  animatedText: string = ''; // Texte animé à afficher
  private fullText: string = 'Writing a better future together!';
  private index: number = 0;

  ngOnInit(): void {
    this.animateText();
  }

  animateText(): void {
    if (this.index < this.fullText.length) {
      this.animatedText += this.fullText.charAt(this.index);
      this.index++;
      setTimeout(() => this.animateText(), 100); // Vitesse d'écriture
    }
  }
}
