import { environment } from '../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Consulation } from './consulation';
import { tap } from  'rxjs/operators';
// import * as jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class ConsulationService {

  constructor(private http: HttpClient) { }

  list () {
    return this.http.get<Consulation[]>(`${environment.api}consultas/`)
      .pipe(
        tap(console.log)
      );
  }
}
