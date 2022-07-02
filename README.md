## PI3

### SISTEMA DE AQUISIÇÃO DE PRESSÃO DE AR COMPRIMIDO PLANTA INDUSTRIAL

#### 1. Proposta Trabalho

O presente trabalho tem a proposta do desenvolvimento de um sistema de aquisição de dados de pressão, de uma planta industrial.

Este sistema deverá fazer a aquisição de pressão periódica, armazenar em sua memória local, disponibilizar a informação em um dispaly gráfico como também um gráfico de comportamento da pressão em função do tempo, localmente.

Este sistema será conectado a rede local através de uma interface ethernet, sendo implementado um servidor local, para acesso dos dados remotamente.

Por fim será implementado uma interface para computador para acesso dos dados e visualizão gráfica das variáveis.


#### 2. Planta

A planta na qual será instalado os sistema é composta por três centrais de geração de ar comprimido, composta por 12 geradores, com uma capacidade máxima de 191m3/min e uma potência de 1,12MW.
Na figura abaixo tem-se o layout resumido da planta.

![layout_1.png](https://raw.githubusercontent.com/edneif/PI3/9d93a5eff6fc5123885bc35ade6224d1cf54fb85/pdf/figuras/layout_1.png)



 ### 3.Implementação do Projeto

#### 3.1 Hardware
 
#### 3.1.1 Hardware Processador

O hardware de processamento selecionado para o projeto é o STM32F746 Discovery Kit da ST. 
Este kit embarca um processador ARM Cortex M7 o **STM32F746NG** de 216MHz, 462MIPS, um display gráfico de 4.3" uma porta Ethernet, conector ARDUINO Uno. Na Figura abaixo tem-se a imagem da placa de desenvolvimento.


![32F746GDISCOVERY](https://user-images.githubusercontent.com/47660021/162569096-981dd325-8ecb-4b37-af0f-9166579ac6fd.png)

Este kit de desenvolvimento foi escolhido por já ter integrado o display gráfico, uma interface ethernet e um conector de expansão de fácil uso, como também o autor deste trabalho já o dispor. Abaixo o link do manual deste hardware [STM32F746 Discovery Kit Manual](https://github.com/edneif/git/blob/main/pdf/um1907-discovery-kit-for-stm32f7-series-with-stm32f746ng-mcu-stmicroelectronics.pdf)

Neste conector de expansão é acoplado um hardware desenvolvido pelo autor que proverá  alimentação, condicionará e isolará os sinais entre trandutores e STM32F746.


#### 3.1.2 Hardware de expansão

A placa de expanção de Hardware terá a finalidade de condicionar e isolar os sinais. A alimentenção do sistema é de 24VDC, definida devido ao grande uso e disponibilidade deste nível de tensão em ambientes industriais. As funcões da placa de expanção de hardware é mostrada na figura abaixo.

![HARDWARE_INTERFACE_1.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/HARDWARE_INTERFACE_1.png)


É previsto na placa de extenção de hardware uma saída 12VDC que deverá alimentar o STM32F746G a partir de uma tensão de entrada de 24VDC, oito entradas digitais isoladas, quatro saídas a rele, 6 entradas analógicas de 0-10VDC isoladas.


#### 3.1.2.1 Esquemático STM32F746 Discovery Kit 

Abaixo tem-se o esquemático resumido da placa de desenvolvimento STM32F746 Discovery Kit.

![esquemático_STM32F746 Discovery Kit.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/esquem%C3%A1tico_STM32F746%20Discovery%20Kit.png)

Pode-se acessar o esquemático completo através do link [Esquemático -STM32F46 Discovery Kit](https://github.com/edneif/PI3/blob/f6d6d0a415206b4271bded015b3e382bf827c5eb/pdf/figuras/en.mb1191-F746NGH6-C01_schematic.pdf)


#### 3.1.2.2 Esquemático Placa Expanção


#### 3.1.2.3 Layout Placa Expanção

Para projeto da placa de expanção foi utilizado o software de projeto de placas de circuito impresso o  Kicad 6.0. A página oficial do Kicad pode ser acessada no link [https://www.kicad.org](https://www.kicad.org/)

Abaixo tem-se o layout final e as visualizações 3D do projeto.

![PCB_01](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_1.png)

![PCB_2.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_2.png)

![PCB_3.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_3.png)

![PCB_4.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_4.png)

![PCB_5.PNG](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_5.png)

![PCB_6.PNG](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_6.png)

![PCB_7.PNG](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/PCB_7.png)


#### 3.1.3 Transdutor de Pressão

Para adquirir os dados de pressão, faz-se necessário um transdutor de pressão. O transdutor escolhido é da faixa de 0 a 10 bar, sabendo-se que a rede de ar comprimido opera em 6 bar, e como saida elétrica 0 a 10V.
![transdutor.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/transdutor.png)

Verificou o  mesmo utilizando um calibrador de manometros.

![verificador_manometro.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/verificador_manometro.png)


|Pressão (bar)  | Saída (V)  |
|--|--|
| 0,0 | 0,1 |
| 1,0 | 1,0 |
| 2,0 | 2,0 |
| 3,0 | 3,0 |
| 4,0 | 4,0 |
| 5,0 | 6,0 |
| 6,0 | 6,0 |
| 7,0 | 7,0 |
| 8,0 | 8,0 |
| 9,0 | 9,0 |
| 10,0 | 9,8 |


### 3.2 Software

#### 3.2.1 Software Firmware STM32

Para  implementação do projeto no ARM Cortex foi utizado a IDE da próprima ST, o STM32IDE CUBE, que poder ser acessado no link [https://www.st.com/en/development-tools/stm32cubeide.html](https://www.st.com/en/development-tools/stm32cubeide.html).

Foi utilizado o freertos [https://www.freertos.org/](https://www.freertos.org/) como base do programa, seguindo o fluxograma  abaixo:

![stm32_fluxograma](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/fluxograma_stm32.png)
[Fluxograma stm32](https://github.com/edneif/PI3/blob/main/pdf/figuras/fluxograma_stm32.pdf)

Conforme fluxograma acima foi utilizado [TouchGFX](https://www.st.com/en/development-tools/touchgfxdesigner.html), uma ferramenta disponibilizada pela própria ST, para simplicar a utilização de displays gráficos. Abaixo tem-se as telas criadas.

![viewScreen1](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/Viewscreen1.png)

![ViewScreen2](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/Viewscreen2.png)

![ViewScreen3](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/Viewscreen3.png)

#### 3.2.2 Software Banco de Dados

Para armazenamento das informações usou-se [postgresql](https://www.postgresql.org/), um database open source. A estrutura do banco de dados verifica-se no fluxograma abaixo.
![BancoDados_1.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/BancoDados_1.png)

Utilizou-se a ferramenta [pgadmin](https://www.pgadmin.org/download/), para acesso ao banco de dados, facilitando o seu uso.
![pgadmin.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/pgadmin.png)

#### 3.2.2 Software Captura Dados

Para comunicar com a placa desenvolvida, adquirindo os dados lidos e salvando no bando de dados, uma estrutura de rede é necessária para a aplicação. Abaixo tem-se um exemplo de rede.

![rede_1.png](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/rede_1.png)

Este serviço conecta-se ao banco de dados, faz uma conexão com a placa, recebe os dados e salva no banco. Algumas bibliotecas de python foram utilizadas como [psycopg2](https://www.psycopg.org/docs/) para conexão com o banco de dados, o cliente TCP foi usado a biblioteca [sockets](https://docs.python.org/pt-br/3/howto/sockets.html).


#### 3.2.3 Software Web Aplications

Para diponibilizar os dados na rede, escreveu-se um programa em python, cuja função é ler do banco de dados, cuja biblioteca principal utilizada foi a [psycopg2](https://www.psycopg.org/docs/) , e disponibilizar via web aplication utilizando [dash](https://dash.plotly.com/).

Abaixo tem-se o gráfico rodando em tempo real que pode ser acessado de qualquer parte da rede interna por um browser como google crome.

![enter image description here](https://raw.githubusercontent.com/edneif/PI3/main/pdf/figuras/resultado_1.png)