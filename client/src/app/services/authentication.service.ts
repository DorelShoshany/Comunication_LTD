import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(private httpClient: HttpClient,
    private router: Router) { }

  public async login(email: string, password: string) {
    const url = "/api/login";
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    await this.httpClient.post(url, formData, {
      responseType: 'json',
    }).toPromise();
    this.router.navigate(['personal']);
  }

  public isAuthenticated(): boolean {
    return this.getCookieValue('access_token') != null;
  }


  private getCookieValue(name: string) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2)
      return parts.pop().split(';').shift();
  }
}
