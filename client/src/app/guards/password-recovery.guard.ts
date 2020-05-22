import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { PasswordRecoveryServiceService } from '../services/password-recovery-service.service';


@Injectable({
  providedIn: 'root'
})
export class PasswordRecoveryGuard implements CanActivate {
  constructor(private router: Router,
    private passwordRecovery: PasswordRecoveryServiceService) {

  }
  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): boolean {
    if (this.passwordRecovery.isAuthenticatedToChangePassword()) {
      return true;
    } else {
      this.router.navigate(['forgotYourPassword']);
      return false;
    }
  }

}
