import { environment } from '../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Consultation } from './consultation';
import { tap } from  'rxjs/operators';
// import * as jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class ConsultationService {

  constructor(private http: HttpClient) { }

  list () {
    return this.http.get<Consultation[]>(`${environment.api}consultas/`)
      .pipe(
        tap()
      );
  }

  delete(id: number) {
    return this.http.delete(`${environment.api}consultas/${id}`);
  }
}
