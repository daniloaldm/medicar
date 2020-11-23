import { environment } from '../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Consultation } from './consultation';
import { Schedule } from './schedule';
import { catchError, tap } from  'rxjs/operators';

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

  getSchedule() {
    return this.http.get<Schedule>(`${environment.api}agendas/`)
      .pipe(tap());
  }

  getScheduleByMedicoId(id: number) {
    return this.http.get<Schedule[]>(`${environment.api}agendas/?medico=${id}`)
    .pipe(tap());
  }

  setConsultation(agendamento: any) {
    return this.http.post<any>(`${environment.api}consultas/`, agendamento)
    .toPromise()
    .catch(err => {
      return "Error"
    });
  }
}
