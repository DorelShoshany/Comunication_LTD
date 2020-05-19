import { Component, OnInit } from '@angular/core';
import { PasswordRecoveryServiceService } from 'src/app/services/password-recovery-service.service';

@Component({
  selector: 'app-password-recovery',
  templateUrl: './password-recovery.component.html',
  styleUrls: ['./password-recovery.component.scss']
})
export class PasswordRecoveryComponent implements OnInit {
  public email;
  public token;
  public errorMessage;

  constructor(private passwordRecoveryServiceService: PasswordRecoveryServiceService) { }

  ngOnInit(): void {
  }

  public async postPasswordRecovery() {
    try {
      await this.passwordRecoveryServiceService.postPasswordRecovery(this.email, this.token);
    } catch {
      this.errorMessage = "Email or token is incorrect";
    }
  }


}
