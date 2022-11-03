# PSR - TP2

Projeto criado no âmbito da UC Programação de Sistemas Robóticos, Departamento de Engenharia Mecânica, Universidade de Aveiro.

**Objetivo:** Desenvolver uma aplicação de Augmented Reality Paint, em que o utilizador poderá pintar uma tela com recurso a um objeto colorido e a uma câmera.

---

## Autores:
* André Cabaço
* Nuno Cunha
* Carlos Santos

---
## Funcionalidades:
* Color Segmenter (o utilizador define em tempo real os parâmetros da fonte colorida de acordo com o ambiente à sua volta)
* Modo normal (o utilizador pinta uma tela branca)
* Modo Use Shake Detection (o programa previne o ruído de movimento e possibilita o uso do rato para pintar)
* Modo Use Video Stream (o utilizador pode usar a imagem capturada como tela)
* Modo Pintura Numerada (o utilizador pinta uma figura legendada com o objetivo de fazer o maior score possível)

---

## Instrucões:
Para o bom aproveitamento da aplicação, o utilizador deve correr primeiro a funcionalidade Color Segmenter para ajustar a deteção da fonte e só depois usar os diferentes modos de utilização.

---
## Comandos para inicializar (terminal):
**Color Segmenter**
```./color_segmenter.py```

**Modo Normal**
```./ar_paint --json limits.json```

**Modo Use Shake Detection**
```./ar_paint --json limits.json -usp```

**Modo Use Video Stream**
```./ar_paint --json limits.json -uvs```

**Modo Pintura Numerada**
```./ar_paint --json limits.json -np```

![](https://user-images.githubusercontent.com/101104928/199628173-14010079-d7e1-492a-bafc-bff326fbfe5f.gif)
