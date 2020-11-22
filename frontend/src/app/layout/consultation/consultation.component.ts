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

  constructor(
    private service: ConsultationService, 
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    // let { value } = this.form;
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

  
  // enableMedico() {

  // }

  onChangeEspecialidade(event) {
    console.log(event.value);
    let especialidade = this.form.get('especialidade');
    console.log(especialidade.value);
    let nome = this.form.get('nome');
    console.log(nome.value);
  }


}
