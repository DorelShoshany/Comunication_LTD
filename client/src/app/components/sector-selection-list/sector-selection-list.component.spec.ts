import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SectorSelectionListComponent } from './sector-selection-list.component';

describe('SectorSelectionListComponent', () => {
  let component: SectorSelectionListComponent;
  let fixture: ComponentFixture<SectorSelectionListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SectorSelectionListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SectorSelectionListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
