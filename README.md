# API Smart Finance

Back-end desenvolvido em Django Rest Framework para o aplicativo [Smart Finance](https://github.com/IsabelaRezendeB/TCC)

## Requisitos
1. Instalar o [Django Rest Framework](https://www.django-rest-framework.org/) e suas devidas dependências expecificadas.
2. Utilizei o [Visual Studio Code](https://code.visualstudio.com/) mas também é possível utilizar outro editor de sua preferência.
3. Para ver a funcionalidade da aplicação, recomendo utilizar o [Postman](https://www.postman.com/downloads/), a URL /swagger ou qualquer plataforma de sua preferência que execute teste de API. 

## Execução
1. Primeiramente, digite no terminal para clonar o repositório:
    ```
    git clone https://github.com/IsabelaRezendeB/API_SmartFinance.git
    ```

2. Após instalar o projeto, digite no terminal o seguinte comando para criar uma máquina virtual
    ```
    python -m venv ./venv
    ```
3. Para iniciá-la:
    ```
    venv\Scripts\Activate.ps1
    ```
4. Para fazer as migrations do Model:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
5. Para executar o projeto:
    ```
    python manage.py runserver
    ```
6. Para executar os testes:
    ```
    python manage.py test
    ```

## Endpoints
É possível visualizar todos os endpoints quando você roda o servidor e acessa a URL http://127.0.0.1:8000/swagger/
### **Carteiras**: 
`GET` /carteiras/\
`POST` /carteiras/\
`GET` /carteiras/{id}/\
`PUT` /carteiras/{id}/\
`PATCH` /carteiras/{id}/\
`DELETE` /carteiras/{id}/\
### **Usuários**: 
`GET` /usuarios/\
`POST` /usuarios/\
`GET` /usuarios/{UID}/\
`PUT` /usuarios/{UID}/\
`PATCH` /usuarios/{UID}/\
`DELETE` /usuarios/{UID}/\
`GET` /usuarios/?q={carteira_id}
### **Ações**: 
`GET` /acoes/\
`POST` /acoes/\
`GET` /acoes/{id}/\
`PUT` /acoes/{id}/\
`PATCH` /acoes/{id}/\
`DELETE` /acoes/{id}/\
`GET` /acoes/?q={carteira_id}
### **Ações filtrados por carteira**: 
`GET` /acoescarteira/{carteira_id}/{identificador}/\
### **Histórico**: 
`GET` /historico/\
`POST` /historico/\
`GET` /historico/{id}/\
`PUT` /historico/{id}/\
`PATCH` /historico/{id}/\
`DELETE` /historico/{id}/\
`GET` /historico/?q={carteira_id}

## Equipe de Desenvolvimento


<table>
  <tr>
    <td align="center">
      <a href="https://github.com/GualterMM">
        <img src="https://avatars.githubusercontent.com/u/35864822?v=4" width="100px;" alt="Foto do Gualter Machado no GitHub"/><br>
        <sub>
          <b>Gualter Machado</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/IsabelaRezendeB">
        <img src="https://avatars.githubusercontent.com/u/49520751?v=4" width="100px;" alt="Foto da Isabela Rezende no GitHub"/><br>
        <sub>
          <b>Isabela Rezende</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/VictoriaRBrito">
        <img src="https://avatars.githubusercontent.com/u/82007104?v=4" width="100px;" alt="Foto da Victoria Brito no GitHub"/><br>
        <sub>
          <b>Victoria Brito</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
