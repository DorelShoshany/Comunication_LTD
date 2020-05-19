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
  public error = "err";
  public errorMessage = '';

  constructor(private httpClient: HttpClient,
    private router: Router) { }

  ngOnInit(): void {
  }


  public async isFormValid() {
    if (this.registerModel.firstName.length == 0) {
      await alert("Please enter first name");
      return await false;
    }
    else if (this.registerModel.lastName.length == 0) {
      alert("Please enter last name");
      return false;
    }
    else if (this.registerModel.password.length == 0) {
      alert("Please enter last name");
      return false;
    }
    else if (this.registerModel.password.length == 0) {
      alert("Please enter last name");
      return false;
    }
    else if (this.registerModel.sectorId == null) {
      alert("Please select sector");
      return false;
    }
    else if (this.registerModel.password) {
      alert("Please select sector");
      return false;
    }
    else {
      return await true;
    }

  }

  public async sendFormRegistetion() {
    try {
      const url = "/api/register";
      const formData = new FormData()
      formData.append("firstName", this.registerModel.firstName);
      formData.append("lastName", this.registerModel.lastName);
      formData.append("email", this.registerModel.email);
      formData.append("password", this.registerModel.password);
      formData.append("sectorId", this.registerModel.sectorId);

      await this.httpClient.post(url, formData, {
        responseType: 'json',
      }).toPromise();
      this.router.navigate(['personal']);
    }
    catch (err) {
      this.errorMessage = err.error;
    }
  }

}
