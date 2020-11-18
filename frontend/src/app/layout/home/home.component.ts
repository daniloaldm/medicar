import { ConsulationService } from './../shared/consulation.service';
import { Component, OnInit } from '@angular/core';
import { Consulation } from './../shared/consulation';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  consulations: Consulation[];
  user = localStorage.getItem('username');

  constructor(private service: ConsulationService) { }

  ngOnInit() {
    this.service.list()
      .subscribe(dados => this.consulations = dados);
  }

}
