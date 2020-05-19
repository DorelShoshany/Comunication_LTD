import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class PasswordRecoveryServiceService {

  constructor(private httpClient: HttpClient,
    private router: Router) { }

  public async askForPasswordRecovery(email: string) {
    const url = "/api/forgotYourPassword";
    const formData = new FormData();
    formData.append("email", email);

    await this.httpClient.post(url, formData, {
    }).toPromise();
    this.router.navigate(['passwordRecovery']);
  }

  public async postPasswordRecovery(email: string, token: string) {
    const url = "/api/passwordRecovery";
    const formData = new FormData();
    formData.append("email", email);
    formData.append("token", token);
    await this.httpClient.post(url, formData, {
    }).toPromise();
    this.router.navigate(['changePassword']);
  }

  public async postChangePassword(password: string) {
    const url = "/api/changePassword";
    const formData = new FormData();
    formData.append("password", password);
    await this.httpClient.post(url, formData, {
    }).toPromise();
    this.router.navigate(['home']);
  }



}
