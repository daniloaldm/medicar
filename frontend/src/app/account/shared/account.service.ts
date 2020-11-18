import { environment } from './../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
// import * as jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor(private http: HttpClient) { }

  async login(user: any) {
    const result = await this.http.post<any>(`${environment.api}auth/jwt/create/`, user).toPromise();
    if (result && result.access) {
      window.localStorage.setItem('token', result.access);
      window.localStorage.setItem('username', user['username']);
      return true;
    }

    return false;
  }

  async createAccount(account: any) {
    const result = await this.http.post<any>(`${environment.api}auth/users/`, account).toPromise();
    return result;
  }
}
