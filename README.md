# IpAPI 
![Logo](https://user-images.githubusercontent.com/82342478/154879274-7b6e7a24-6c41-47c5-aa0e-e571d3b31729.PNG)

### Overview
Está API construida com django Rest Framework permite visualizar dados sobre a localização de certo IP fazendo uma requisição para uma API (http://ip-api.com)
A API permite rquesições GET no seguinte endpoint : /api?query=($ip)
Onde a variavel 'query' é uma string e recebe o valor do IP.

### Inicializando
Requesitos: 
- Docker

```Para inicializar locamente 
Clone esse repositorio: 
$ git clone https://github.com/zycki-gif/IpAPI.git
```

```
#Na pasta local abra o terminal:
$ docker-compose up --build
```


```
# Rodando Localmente

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 3.2.6, using settings 'api_config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Usando
```Abra seu navegador e va para o endpoint informando o IP de consulta: http://localhost:8000/api?query=24.48.0.1```

![works](https://user-images.githubusercontent.com/82342478/154881116-d3308e61-3285-4b54-8454-b546fba0082c.PNG)
