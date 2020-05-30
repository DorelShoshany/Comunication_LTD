import { Component } from '@angular/core';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Title } from "@angular/platform-browser";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'client';

  constructor(public authentication: AuthenticationService, private titleService: Title) {
    this.titleService.setTitle("Communication LTD")
  }
}
