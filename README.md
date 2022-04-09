## PI3

### SISTEMA DE AQUISIÇÃO DE PRESSÃO DE AR COMPRIMIDO PLANTA INDUSTRIAL

 1. Proposta Trabalho

O presente trabalho tem a proposta do desenvolvimento de um sistema de aquisição de dados de pressão, de uma planta industrial.

Este sistema deverá fazer a aquisição de pressão periódica, armazenar em sua memória local, disponibilizar a informação em um dispaly gráfico como também um gráfico de comportamento da pressão em função do tempo, localmente.

Este sistema será conectado a rede local através de uma interface ethernet, sendo implementado um servidor local upd, para acesso dos dados remotamente.

Por fim será implementado uma interface para computador para acesso dos dados e visualizão gráfica das variáveis.


2. Planta

A planta na qual será instalado os sistema é composta por três centrais de geração de ar comprimido, composta por 12 geradores, com uma capacidade máxima de 191m3/min e uma potência de 1,12MW.
Na figura abaixo tem-se o layout resumido da planta.


![layout_1](https://user-images.githubusercontent.com/47660021/162568647-0a24d110-9b0b-4892-9c68-00477322cb1b.png)


 3.Especificações Projeto

3.1 Hardware 

O Hardware selecionado para o projeto é o STM32F746 Discovery Kit.
Este kit embarca um processador ARM Cortex M7 o **STM32F746NG** de 216MHz, 462MIPS, um display gráfico de 4.3" uma porta Ethernet, conector ARDUINO Uno.


