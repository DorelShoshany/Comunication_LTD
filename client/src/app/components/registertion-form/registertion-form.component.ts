import { Component, OnInit } from '@angular/core';
import { RegisterModel } from 'src/app/model/register-model';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registertion-form',
  templateUrl: './registertion-form.component.html',
  styleUrls: ['./registertion-form.component.scss']
})
export class RegistertionFormComponent implements OnInit {
  public registerModel = new RegisterModel();

  public errorMessage = '';

  constructor(private httpClient: HttpClient,
    private router: Router) { }

  ngOnInit(): void {
  }

  public async sendFormRegistetion() {
    const url = "/api/register";
    const formData = new FormData()
    formData.append("firstName", this.registerModel.firstName);
    formData.append("lastName", this.registerModel.lastName);
    formData.append("email", this.registerModel.email);
    formData.append("password", this.registerModel.password);
    formData.append("sectorId", this.registerModel.sectorId);
    try {
      await this.httpClient.post(url, formData).toPromise();
      this.router.navigate(['personal']);
    } catch {
      this.errorMessage = "User name or password is incorrect";
    }

  }
}

