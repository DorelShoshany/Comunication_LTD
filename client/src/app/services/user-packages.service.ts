import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PackageOfferring } from '../models/package-offerring';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable } from 'rxjs';
import { flatMap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserPackagesService {
  private subject = new BehaviorSubject<void>(null);

  constructor(private httpClient: HttpClient, private router: Router) {

  }

  public async getOfferings(): Promise<PackageOfferring[]> {
    const url = '/api/packagesOfferings';
    return await this.httpClient.get<PackageOfferring[]>(url).toPromise();
  }

  public getPackagesPurchases(): Observable<PackageOfferring[]> {
    const url = '/api/yourPackages';
    return this.subject.pipe(
      flatMap(() => this.httpClient.get<PackageOfferring[]>(url))
    );
  }

  public async postPackage(offerId: string) {
    const url = '/api/buypackage';
    const formData = new FormData();
    formData.append("id", offerId);
    await this.httpClient.post(url, formData, {
      responseType: 'json',
    }).toPromise();
    this.subject.next();

  }

}
