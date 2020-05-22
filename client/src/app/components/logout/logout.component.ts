import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.scss']
})
export class LogoutComponent implements OnInit {
  public errorMessage = "";
  constructor(private httpClient: HttpClient, private router: Router) {
    this.logOut();
  }

  ngOnInit(): void {
  }


  public async logOut() {
    try {
      const isConfirm = confirm(`you are about to logout, Are you sure?`);
      if (isConfirm) {
        const url = '/api/logout';
        return await this.httpClient.get(url).toPromise();
      }
    }
    catch (err) {
      this.errorMessage = err.error;
    }
  }


}
