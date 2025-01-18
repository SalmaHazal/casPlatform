import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageWithNavbarSidebarComponent } from './page-with-navbar-sidebar.component';

describe('PageWithNavbarSidebarComponent', () => {
  let component: PageWithNavbarSidebarComponent;
  let fixture: ComponentFixture<PageWithNavbarSidebarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PageWithNavbarSidebarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageWithNavbarSidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
