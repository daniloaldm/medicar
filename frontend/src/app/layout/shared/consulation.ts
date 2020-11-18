export interface Consulation {
    id: number;
    dia: string;
    horario: string;
    data_agendamento: string;
    medico: {
      id: number;
      crm: string;
      nome: string;
      especialidade: {
        id: number;
        especialidade: string;
      }
    }
}
