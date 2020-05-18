import { Component, OnInit } from '@angular/core';
import { UserPackagesService } from 'src/app/services/user-packages.service';
import { PackageOfferring } from 'src/app/models/package-offerring';

@Component({
  selector: 'app-users-packages-offerring',
  templateUrl: './users-packages-offerring.component.html',
  styleUrls: ['./users-packages-offerring.component.scss']
})
export class UsersPackagesOfferringComponent implements OnInit {
  public offerings: PackageOfferring[];

  constructor(private userPackages: UserPackagesService) { }

  async ngOnInit() {
    this.offerings = await this.userPackages.getOfferings();

  }

  public buyPackage() {
    console.log("dorel")
  }


}
