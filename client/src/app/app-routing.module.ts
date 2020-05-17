import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { PersonalAreaComponent } from './components/personal-area/personal-area.component';
import { AuthenticateGuard } from './guards/authenticate.guard';
import { AnonymousGuard } from './guards/anonymous.guard';
import { RegistertionFormComponent } from './components/registertion-form/registertion-form.component';



const routes: Routes = [
  { path: '', component: HomePageComponent },
  { path: 'home', component: HomePageComponent },
  { path: 'login', component: LoginComponent, canActivate: [AnonymousGuard] },
  { path: 'personal', component: PersonalAreaComponent, canActivate: [AuthenticateGuard] },
  { path: 'register', component: RegistertionFormComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
