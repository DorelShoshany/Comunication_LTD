import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PackageOfferring } from '../models/package-offerring';

@Injectable({
  providedIn: 'root'
})
export class UserPackagesService {

  constructor(private httpClient: HttpClient) { }

  public async getOfferings(): Promise<PackageOfferring[]> {
    const url = '/api/packagesOfferings';
    return await this.httpClient.get<PackageOfferring[]>(url).toPromise();
  }

  public async getPackagesPurchases(): Promise<PackageOfferring[]> {
    const url = '/api/yourPackages';
    return await this.httpClient.get<PackageOfferring[]>(url).toPromise();
  }



}
