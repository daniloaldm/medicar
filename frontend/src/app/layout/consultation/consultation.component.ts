import { Component, OnInit } from '@angular/core';
import { Schedule } from '../shared/schedule';
import { ConsultationService } from '../shared/consultation.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-consultation',
  templateUrl: './consultation.component.html',
  styleUrls: ['./consultation.component.css']
})
export class ConsultationComponent implements OnInit {

  form: FormGroup;
  schedules: Schedule[];
  medicoED = true;
  dataED = true;
  horaED = true;
  buttonED = true;


  constructor(
    private service: ConsultationService, 
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      especialidade: [null],
      nome: [null],
      dia: [null],
      horarios: [null]
    });
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
    this.medicoED = false;
    console.log(this.schedules);
  }

  onChangeMedico(event) {
    console.log(event.value);
    this.dataED = false;
  }

  onChangeData(event) {
    console.log(event.value);
    this.horaED = false;
  }

  onChangeHora(event) {
    console.log(event.value);
    this.buttonED = false;
  }
}
