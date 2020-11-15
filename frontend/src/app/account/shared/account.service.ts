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
    if (result && result.access_token) {
      window.localStorage.setItem('token', result.access);
      return true;
    }

    return false;
  }

  createAccount(account: any) {
    return new Promise((resolve) => {
      resolve(true);
    });
  }
}
