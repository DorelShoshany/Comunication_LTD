import { TestBed } from '@angular/core/testing';

import { PasswordRecoveryGuard } from './password-recovery.guard';

describe('PasswordRecoveryGuard', () => {
  let guard: PasswordRecoveryGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(PasswordRecoveryGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
