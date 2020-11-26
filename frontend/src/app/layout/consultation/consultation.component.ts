import { Component, OnInit } from '@angular/core';
import { Schedule } from '../shared/schedule';
import { ConsultationService } from '../shared/consultation.service';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { normalizeGenFileSuffix } from '@angular/compiler/src/aot/util';
import { Router } from '@angular/router';
import { Consultation } from '../shared/consultation';


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
  consultations: Consultation[];

  medicosFilter = [];
  dataFilter = [];
  horarioFilter = [];
  horarioMap = [];
  agendaId = '';
  horaSelecionada = '';
  diaSelecionado = '';

  constructor(
    public service: ConsultationService, 
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      especialidade: [null],
      nome: [null],
      dia: [null],
      horarios: [null]
    });

    this.consultarMedicos();
    this.consultas();
  }

  async consultarMedicos() {
    await this.service.getSchedule().subscribe(dados => this.schedules = dados);
  }

  async consultas() {
    await this.service.list().subscribe(dados => this.consultations = dados);
  }

  async onSubmit() {
    try {
      const payload = {
        id_agenda: this.agendaId,
        horario: this.horaSelecionada
      };

      if(this.validForm(payload)){
        const result = await this.service.setConsultation(payload);
        this.router.navigate(['']).then(() => {
          window.location.reload();
        });
      }else{
        alert('Já existe uma consulta com esse médico marcada para o mesmo dia e horário selecionado!');
      }

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
    this.diaSelecionado = document.getElementById("dia-selecionado").textContent;
    const medicos = this.schedules;

    const medicoId = event.value;

    this.horarioFilter = [];

    Object.values(medicos).find(medico => {
      if (medico.id === medicoId) {
        this.agendaId = event.value;
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
    this.horaSelecionada = event.value;

    this.buttonED = false;
  }

  validForm(payload){
    const consultationExists = this.consultations;
    let auxBoolean = true;
    Object.values(consultationExists).find(consultation => {
      let consultationFormated = consultation.horario.substring(0, consultation.horario.length - 3);
      this.diaSelecionado = this.diaSelecionado.split("/").reverse().join("");
      this.diaSelecionado = this.diaSelecionado.replace(" ", "-");
      if ((consultationFormated == payload.horario) && (consultation.dia == this.diaSelecionado)) {
        auxBoolean = false;
      }
    });
    return auxBoolean;
  }
}
