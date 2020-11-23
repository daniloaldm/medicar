import { Component, OnInit } from '@angular/core';
import { Schedule } from '../shared/schedule';
import { ConsultationService } from '../shared/consultation.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { normalizeGenFileSuffix } from '@angular/compiler/src/aot/util';


@Component({
  selector: 'app-consultation',
  templateUrl: './consultation.component.html',
  styleUrls: ['./consultation.component.css']
})
export class ConsultationComponent implements OnInit {

  form: FormGroup;
  schedules: Schedule;
  medicoED = true;
  dataED = true;
  horaED = true;
  buttonED = true;

  medicosFilter = [];
  dataFilter = [];
  horarioFilter = [];
  horarioMap = [];

  constructor(
    public service: ConsultationService, 
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    // let {value}  = this.form;
    this.form = this.formBuilder.group({
      especialidade: [null],
      nome: [null],
      dia: [null],
      horarios: [null]
    });

    this.consultarMedicos();
  }

  async consultarMedicos() {
    await this.service.getSchedule().subscribe(dados => this.schedules = dados);
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
    const especialidade = event.value;
    
    const medicos = this.schedules;

    this.medicosFilter = [];

    Object.values(medicos).find(medico => {
      if (medico.medico.especialidade.especialidade === especialidade) {
        this.medicosFilter.push(medico);
      }
    });

    this.medicoED = false;
  }

  onChangeMedico(event) {
    const medicos = this.schedules;

    const medicoId = event.value;

    this.dataFilter = [];

    Object.values(medicos).find(medico => {
      if (medico.id === medicoId) {
        this.dataFilter.push(medico);
      }
    });

    this.dataED = false;
  }

  onChangeData(event) {
    console.log(event.value);

    const medicos = this.schedules;

    const medicoId = event.value;

    this.horarioFilter = [];

    Object.values(medicos).find(medico => {
      if (medico.id === medicoId) {
        this.horarioFilter.push(medico.horarios);
      }
    });

    this.horarioMap = [];

    this.horarioFilter.map((horario) => {
      horario.map(hor => {
        this.horarioMap.push(hor);
      })
    })
    
    this.horaED = false;
  }

  onChangeHora(event) {
    this.buttonED = false;
  }
}
