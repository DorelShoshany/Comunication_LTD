import { TestBed } from '@angular/core/testing';

import { UserPackagesService } from './user-packages.service';

describe('UserPackagesService', () => {
  let service: UserPackagesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UserPackagesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
