import { TestBed } from '@angular/core/testing';

import { PasswordRecoveryServiceService } from './password-recovery-service.service';

describe('PasswordRecoveryServiceService', () => {
  let service: PasswordRecoveryServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PasswordRecoveryServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
