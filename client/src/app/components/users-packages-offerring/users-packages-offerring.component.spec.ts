import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UsersPackagesOfferringComponent } from './users-packages-offerring.component';

describe('UsersPackagesOfferringComponent', () => {
  let component: UsersPackagesOfferringComponent;
  let fixture: ComponentFixture<UsersPackagesOfferringComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UsersPackagesOfferringComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UsersPackagesOfferringComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
