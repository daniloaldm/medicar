import { Component, OnInit } from '@angular/core';
import { Schedule } from '../shared/schedule';
import { ConsultationService } from '../shared/consultation.service';

@Component({
  selector: 'app-consultation',
  templateUrl: './consultation.component.html',
  styleUrls: ['./consultation.component.css']
})
export class ConsultationComponent implements OnInit {

  schedules: Schedule[];

  constructor(private service: ConsultationService) { }

  ngOnInit(): void {
    this.service.getSchedule().subscribe(dados => this.schedules = dados);
  }

}
