import { Component, OnInit } from '@angular/core';
import { PackageOfferring } from 'src/app/models/package-offerring';
import { UserPackagesService } from 'src/app/services/user-packages.service';

@Component({
  selector: 'app-user-purchases',
  templateUrl: './user-purchases.component.html',
  styleUrls: ['./user-purchases.component.scss']
})
export class UserPurchasesComponent implements OnInit {
  public packages: PackageOfferring[];
  constructor(private userPackages: UserPackagesService) { }

  async ngOnInit() {
    this.packages = await this.userPackages.getPackagesPurchases();

  }
}
