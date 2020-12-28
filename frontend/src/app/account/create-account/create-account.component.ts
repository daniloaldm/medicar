import { Router } from '@angular/router';
import { AccountService } from './../shared/account.service';
import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})
export class CreateAccountComponent implements OnInit {
  account = {
    username: '',
    email: '',
    password: '',
    password2: ''
  };

  constructor(
    private accountService: AccountService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  async onSubmit() {
    try {
      if(this.account.password == this.account.password2){
        const result = await this.accountService.createAccount(this.account);

        Swal.fire({
          icon: 'success',
          title: 'Usuario cadastrado com sucesso',
          showConfirmButton: false,
          timer: 2000,
        });
        
        this.router.navigate(['/login']);
      }else{
        Swal.fire({
          icon: 'error',
          title: 'Sua senha está diferente da confirmação de senha, por favor, verifique se os campos "Senha" e "Confirmar Senha" estão iguais.',
          showConfirmButton: false,
          timer: 10000,
        });
      }
      
    } catch (error) {
      let msgerror = '';

      Object.keys(error.error).map(variavel => {
        error.error[variavel].map(text => {
            msgerror = msgerror + text + '\n\n'
        })
      });

      Swal.fire({
        icon: 'error',
        title: msgerror,
        showConfirmButton: false,
        timer: 10000,
      });
    }
  }

}
