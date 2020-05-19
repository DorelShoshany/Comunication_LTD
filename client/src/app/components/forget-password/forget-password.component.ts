import { Component, OnInit } from '@angular/core';
import { PasswordRecoveryServiceService } from 'src/app/services/password-recovery-service.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';



@Component({
  selector: 'app-forget-password',
  templateUrl: './forget-password.component.html',
  styleUrls: ['./forget-password.component.scss']
})
export class ForgetPasswordComponent implements OnInit {
  public email;
  public errorMessage;

  constructor(private passwordRecoveryServiceService: PasswordRecoveryServiceService) {
  }

  ngOnInit(): void {
  }

  public async askForPasswordRecovery() {
    try {
      await this.passwordRecoveryServiceService.askForPasswordRecovery(this.email);
    } catch {
      this.errorMessage = "Email is incorrect";
    }
  }


}
