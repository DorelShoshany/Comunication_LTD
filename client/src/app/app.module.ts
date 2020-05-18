import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { PersonalAreaComponent } from './components/personal-area/personal-area.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { UsersPackagesOfferringComponent } from './components/users-packages-offerring/users-packages-offerring.component';
import { RegistertionFormComponent } from './components/registertion-form/registertion-form.component';
import { SectorSelectionListComponent } from './components/sector-selection-list/sector-selection-list.component';
import { UserPurchasesComponent } from './components/user-purchases/user-purchases.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    PersonalAreaComponent,
    HomePageComponent,
    UsersPackagesOfferringComponent,
    RegistertionFormComponent,
    SectorSelectionListComponent,
    UserPurchasesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
