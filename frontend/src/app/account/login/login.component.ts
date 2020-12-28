import { Router } from '@angular/router';
import { AccountService } from './../shared/account.service';
import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  login = {
    username: '',
    password: '',
    checked: false
  };

  constructor(
    private accountService: AccountService,
    private router: Router
  ) { }

  ngOnInit() {
    this.verificarChecked();
  }

  async onSubmit() {
    try {
      const result = await this.accountService.login(this.login);

      Swal.fire({
        icon: 'success',
        title: 'Logado com Sucesso!',
        showConfirmButton: false,
        timer: 2000,
      });

      this.router.navigate(['']).then(() => {
        window.location.reload();
      });
    } catch (error) {
      console.error(error);
      let msgerror = '';

      Object.keys(error.error).map(variavel => {
        msgerror =  error.error[variavel]
      });

      Swal.fire({
        icon: 'error',
        title: msgerror,
        showConfirmButton: false,
        timer: 10000,
      });

    }
  }

  setChecked(checked) {
    this.login.checked = checked;
  }

  verificarChecked(){
    const isChecked = localStorage.getItem('checked'); 
    if(isChecked){
      this.login.username = localStorage.getItem('username');
      this.login.password = localStorage.getItem('password'); 
      this.login.checked = true;
    }
  }
}