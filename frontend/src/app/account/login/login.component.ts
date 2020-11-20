import { Router } from '@angular/router';
import { AccountService } from './../shared/account.service';
import { Component, OnInit } from '@angular/core';

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

      alert("Conectado(a)!");
      this.router.navigate(['']).then(() => {
        window.location.reload();
      });
    } catch (error) {
      alert("Dados Inválidos");
      console.error(error);
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