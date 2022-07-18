# Calculadora de Pitágoras API

<p>Essa API visa calcular as relações entre os lados de um triângulo retângulo 
através dos cálculos feitos por Pitágoras.</p>

## Rodar a Aplicação localmente:
<ul>
  <li>1. Rode o arquivo main da aplicação</li>
  <li>2. Acesse <a href="http://localhost:5000/">http://localhost:5000/</a> no seu navegador</li>
</ul>

## Rodar a Aplicação remotamente:
<p>Acesse o site: <a href="https://calculadora-pitagoras.herokuapp.com/">https://calculadora-pitagoras.herokuapp.com/</a></p>

## Endpoints:
### Para o cálculo da hipotenusa:
<p>GET: /hipotenusa/{cateto_1}/{cateto_2}</p>
<p>Descrição:</p>
<ul>
  <li>cateto_1: Valor do primeiro cateto</li>
  <li>cateto_2: Valor do segundo cateto</li>
</ul>

<p>Resposta:</p>
<ul>
  <li>200: Sucesso!</li>
  <li>400: Erro na Requisição!</li>
  <li>500: Erro na Aplicação!</li>
</ul>

### Para o cálculo dos catetos:
<p>GET: /cateto/{hipotenusa_entrada}/{cateto_entrada}</p>
<p>Descrição:</p>
<ul>
  <li>hipotenusa_entrada: Valor da hipotenusa</li>
  <li>cateto_entrada: Valor do cateto</li>
</ul>

<p>Resposta:</p>
<ul>
  <li>200: Sucesso!</li>
  <li>400: Erro na Requisição!</li>
  <li>500: Erro na Aplicação!</li>
</ul>

## Esquemas:
### Hipotenusa:
{"resultado": string}
### Cateto:
{"resultado": string}

## Tecnologias usadas:
<ul>
  <li>flask</li>
  <li>gunicorn</li>
  <li>flask_cors</li>
</ul>