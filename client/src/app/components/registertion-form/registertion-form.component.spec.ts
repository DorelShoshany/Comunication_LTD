import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistertionFormComponent } from './registertion-form.component';

describe('RegistertionFormComponent', () => {
  let component: RegistertionFormComponent;
  let fixture: ComponentFixture<RegistertionFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegistertionFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistertionFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
