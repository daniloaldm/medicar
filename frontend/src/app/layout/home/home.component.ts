import { ConsultationService } from '../shared/consultation.service';
import { Component, OnInit } from '@angular/core';
import { Consultation } from '../shared/consultation';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  consultations: Consultation[];
  user = localStorage.getItem('username');

  constructor(private service: ConsultationService) { }

  ngOnInit() {
    this.service.list()
      .subscribe(dados => this.consultations = dados);
  }

  delete(consultation){
    this.service.delete(consultation.id).subscribe();
    window.location.reload();
  }

  disconnect(){
    window.localStorage.removeItem('token');
    window.location.reload();
  }
}
