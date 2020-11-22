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

  async onSubmit() {
    try {
      // const result = await this.accountService.login(this.login);

      // alert("Conectado(a)!");
      // this.router.navigate(['']).then(() => {
      //   window.location.reload();
      // });
    } catch (error) {
      alert("Dados Inválidos");
      console.error(error);
    }
  }

  onChangeEspecialidade(event) {
    console.log(event.value);
  }
}
