import { AccountService } from './../shared/account.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})
export class CreateAccountComponent implements OnInit {
  account = {
    username: '',
    email: '',
    password: ''
  };

  constructor(
    private accountService: AccountService
  ) { }

  ngOnInit(): void {
  }

  async onSubmit() {
    try {
      const result = await this.accountService.createAccount(this.account);

      alert("Conta criada com sucesso!");
      console.log(result);
    } catch (error) {
      alert("Dados Inválidos");
      console.error(error);
    }
  }

}
