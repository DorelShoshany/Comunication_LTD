import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { UserPackagesService } from 'src/app/services/user-packages.service';
import { PackageOfferring } from 'src/app/models/package-offerring';

@Component({
  selector: 'app-users-packages-offerring',
  templateUrl: './users-packages-offerring.component.html',
  styleUrls: ['./users-packages-offerring.component.scss']
})
export class UsersPackagesOfferringComponent implements OnInit {
  public offerings: PackageOfferring[];
  public errorMessage = '';

  constructor(private userPackages: UserPackagesService) { }

  async ngOnInit() {
    try {
      this.offerings = await this.userPackages.getOfferings();
    }
    catch (err) {
      this.errorMessage = err.error;
    }
  }

  public async buyPackage(packageOffer: PackageOfferring) {
    try {
      const isConfirm = confirm(`you are about to buy ${packageOffer.name} of ${packageOffer.price}, are you sure?`);
      if (isConfirm) {
        await this.userPackages.postPackage(packageOffer.id);
      }
    }
    catch (err) {
      this.errorMessage = err.error;
    }
  }


}
