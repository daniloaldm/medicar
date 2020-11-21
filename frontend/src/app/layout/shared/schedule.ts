export interface Schedule {
  id: number;
  medico: {
    id: number;
    crm: string;
    nome: string;
    especialidade: {
      id: number;
      especialidade: string;
    }
  }
  dia: string;
  horarios: string;
}
