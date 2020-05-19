import { Component, OnInit } from '@angular/core';
import { PasswordRecoveryServiceService } from 'src/app/services/password-recovery-service.service';

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.scss']
})

export class ChangePasswordComponent implements OnInit {
  public password;
  public errorMessage;

  constructor(private passwordRecoveryServiceService: PasswordRecoveryServiceService) { }

  ngOnInit(): void {
  }


  public async changePassword() {
    try {
      await this.passwordRecoveryServiceService.postChangePassword(this.password);
    } catch {
      this.errorMessage = "password shuld be ";
    }
  }

}
