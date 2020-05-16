import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public email;
  public password;
  public errorMessage = '';

  constructor(private authenticationService: AuthenticationService) {
  }

  ngOnInit() {
  }

  public async login() {
    try {
      await this.authenticationService.login(this.email, this.password);
    } catch {
      this.errorMessage = "User name or password is incorrect";
    }
  }



}