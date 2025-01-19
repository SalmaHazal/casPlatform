import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PotentialSponsorsComponent } from './potential-sponsors.component';

describe('PotentialSponsorsComponent', () => {
  let component: PotentialSponsorsComponent;
  let fixture: ComponentFixture<PotentialSponsorsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PotentialSponsorsComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(PotentialSponsorsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
