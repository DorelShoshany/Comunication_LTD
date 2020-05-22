import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { PersonalAreaComponent } from './components/personal-area/personal-area.component';
import { AuthenticateGuard } from './guards/authenticate.guard';
import { AnonymousGuard } from './guards/anonymous.guard';
import { RegistertionFormComponent } from './components/registertion-form/registertion-form.component';
import { ForgetPasswordComponent } from './components/forget-password/forget-password.component';
import { PasswordRecoveryComponent } from './components/password-recovery/password-recovery.component';
import { ChangePasswordComponent } from './components/change-password/change-password.component';
import { LogoutComponent } from './components/logout/logout.component';



const routes: Routes = [
  { path: '', component: HomePageComponent },
  { path: 'home', component: HomePageComponent },
  { path: 'login', component: LoginComponent, canActivate: [AnonymousGuard] },
  { path: 'personal', component: PersonalAreaComponent, canActivate: [AuthenticateGuard] },
  { path: 'register', component: RegistertionFormComponent },
  { path: 'forgotYourPassword', component: ForgetPasswordComponent },
  { path: 'passwordRecovery', component: PasswordRecoveryComponent },
  { path: 'changePassword', component: ChangePasswordComponent },
  { path: 'logout', component: LogoutComponent }



];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
