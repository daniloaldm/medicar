import { environment } from './../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
// import * as jwt_decode from 'jwt-decode';

interface User {
  username: string;
  password: string;
  checked: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor(private http: HttpClient) { }

  async login(user: User) {
    const result = await this.http.post<any>(`${environment.api}auth/jwt/create/`, user).toPromise();
    if (result && result.access) {
      localStorage.setItem('token', result.access);
      localStorage.setItem('username', user.username);
      
      if(!user.checked){
        localStorage.removeItem('password');
        localStorage.removeItem('checked');
        return true;
      }
      
      localStorage.setItem('password', user.password);
      localStorage.setItem('checked', user.checked.toString());

      return true;
    }

    return false;
  }

  async createAccount(account: any) {
    const result = await this.http.post<any>(`${environment.api}auth/users/`, account).toPromise();
    return result;
  }
}
