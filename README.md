# Projeto Integrador 3 -> TeaWizard
## Aluno: Eric Monteiro dos Reis

### Pitch deck

O TeaWizard é o produto perfeito para os amantes de chá que querem a melhor experiência possível. Com o TeaWizard, você pode controlar automaticamente a sua chaleira através de uma interface web, selecionando o tipo de chá que deseja dentre as opções pré-definidas, como chá verde, chá preto, e muitas outras, ou personalizar o tempo e temperatura para um chá específico que você ama.

O TeaWizard é equipado com um sensor de peso que informa exatamente a quantidade de chá necessária e um sensor de temperatura que controla a água perfeitamente para cada tipo de chá. Além disso, a interface também notifica quando o chá está pronto para ser consumido e avisa o usuário. Dessa forma, você pode aproveitar o seu chá perfeito sem se preocupar com a hora de retirá-lo da chaleira.

O TeaWizard também registra os dados de uso, permitindo que ele aprimore a sua experiência ao longo do tempo com base nas suas escolhas anteriores.

### Funcionamento do Produto
![Untitled Diagram drawio](https://user-images.githubusercontent.com/13921131/224200613-4786aa3b-7943-491e-a420-08372f573c97.png)




Cronograma de atividades a serem desenvolvidas durante o semestre: 

|Data |Atividade a ser desenvolvida  |
|--|--|
| 17/02/2023 |Revisão bibliográfica  |
| 24/02/2023 | Revisão bibliográfica |
| 03/03/2023 |Iniciar a montagem dos materiais de apresentação do projeto  |
| 10/03/2023 | Apresentação inicial do projeto |
| 17/03/2023 |Estudo de documentação do ESP32 para utilização de MicroPython  |
| 24/03/2023 | Testes utilizando MicroPython e os sensores utilizados |
| 31/03/2023 |Testes utilizando MicroPython e os sensores utilizados  |
| 07/04/2023 |Testes da interface web  |
| 14/04/2023 |Testes da interface web  |
| 21/04/2023 | Testes do atuador no projeto |
| 28/04/2023 |Apresentação dos resultados parciais do projeto  |
| 05/05/2023 |Testes de integração  |
| 12/05/2023 | Testes de integração final |
| 19/05/2023 | Roteamento da PCB |
| 26/05/2023 | Roteamento da PCB |
| 02/06/2023 |Confecção da placa final|
| 09/06/2023 |Confecção da placa final|
| 16/06/2023 |Testes da placa final|
| 23/06/2023 |Apresentação final do projeto |
| 30/06/2023 |Recuperação final|

### Requisitos técnicos

Para a implementação das funcionalidades do projeto é necessário a medição de alguns parâmetros que serão chave para o funcionamento correto do sistema. 

- Medição de volume de líquido
- Medição de temperatura da água
- Controle de acionamento
- Armazenamento dos dados de utilização do usuário do sistema
- Temporização
- Comunicação Wi-Fi
- Interface Web

A medição do volume de líquido é necessária por 2 motivos. O primeiro motivo é que o sensor de temperatura que será implementado na chaleira precisa de um nível minimo de liquido para que ele funcione. Na teoria será realizado um furo na chaleira onde será inserido o sensor perto da base dela. O volume mínimo de líquido será definido por um sensor de peso que será instalado na chaleira. A segunda razão da medição é que para garantirmos que o chá tenha um bom sabor, precisamos recomendar para o usuário a quantidade de chá ideal a ser utilizada para a quantidade de líquido inserida. A proporção recomendada será de 2g de chá para cada 200ml de água. A chaleira comprada possuí 1,8L de capacidade porém será imposto no sistema um limite de volume máximo de liquido de 1,2 litros.
A medição será realizada utilizando uma célula de carga em conjunto com o módulo HX711  para obtermos a medição de peso. Este módulo conversor e amplificador HX711 de 24 bits, é normalmente utilizado para amplificar o sinal de dispositivos como células de carga, fazendo a interligação entre essas células e o microcontrolador. Ambos são materiais de baixo custo, porém a célula de carga deve suportar até no máximo 3kg, para garantir que teremos precisão na medição do volume de líquido.

![Untitled Diagram2 drawio](https://user-images.githubusercontent.com/13921131/224203713-c2d3dfb9-bf6d-4f62-ad26-d0b4a07e34fb.png)

A temperatura do chá será medida para garantirmos que dependendo do tipo de chá, estaremos com a temperatura ideal que irá garantir o melhor sabor e também preservando as propriedades bioquimicas do chá (exemplo: chás são ótimos anti-oxidantes e dependendo da temperatura podemos inibir a liberação dessas substâncias).
Para esse projeto será utilizado o sensor DS18B20. Ele possuí alguns features que tornam ele a escolha ideal para esse projeto.

O sensor DS18B20 possuí uma versão a prova d’agua, que é um dos pre-requisitos do projeto, já que estamos trabalhando com a temperatura de um liquido.

- O sensor é one-wire, possuindo 3 fios (2 de alimentação e 1 de dados), fazendo com que ocupe somente um pino GPIO, ponto importante se tratando de sistemas utilizando microcontroladores.

- Possuí range de temperatura de -55°C até 125°C, portanto ele cobre tranquilamente o caso de uso do projeto.

- Precisão de ±0.5°C de -10°C até +85°C.

- Baixo tempo de leitura, abaixo de 750ms.

![image](https://user-images.githubusercontent.com/13921131/224203846-db250be6-c76d-476a-ad91-dd661ea5310c.png)

Para o controle da chaleira será necessário um módulo de acionamento de fácil prototipagem e que suporte a potência do produto. O modulo precisa ser controlado com baixas tensões, já que estamos trabalhando com um microcontrolador. Será utilizado um módulo de acionamento com 2 relés que suporta em 250VAC até 10A, sendo portanto capaz de suportar a corrente necessária para o funcionamento correto da chaleira, que possui potência de 1000 W.

![image](https://user-images.githubusercontent.com/13921131/224204470-13e7083b-ff6d-4173-b714-f4df0f2f5cf3.png)

O projeto irá possuir interface web de comunicação com o usuário pelos seguintes motivos:
- Irá facilitar a interação do usuário com o menu de opções.
- Irá facilitar a visualização dos valores em tempo real.
- É uma forma de interface com usuário mais moderna, comparado a um display LCD.

(Será inserido no futuro uma imagem demonstrando a UI)

O microcontrolador que será utilizado no projeto precisará possuir conexão com WIFI, para realizar a comunicação via web interface com o usuário.
Possuir recursos como bibliotecas e documentação para a prototipagem rápida de um projeto.

O módulo a ser utilizado para esse projeto será o ESP32, por causa dos seguintes motivos.
- O ESP32 tem a possibilidade de trabalhar utilizando MicroPython. Python é uma linguagem que eu possuo mais familiaridade, possuí diversas bibliotecas já disponíveis para diversos sensores, além de ser uma linguagem de fácil prototipagem e debug.
- O ESP32 possuí um módulo WI-FI de fácil configuração e utilização.
- Este microcontrolador é muito utilizado atualmente no desenvolvimento de projetos pessoais, portanto é rico em documentação e exemplos de utilização dos seus recursos.
- O ESP32 possuí a capacidade de salvar valores em memória. Isso será importante futuramente na utilização dos dados de utilização do usuário para a sugestão das melhores experiências possíveis para ele.

![image](https://user-images.githubusercontent.com/13921131/224205037-9e03cdd4-3a20-4177-81ee-c6d7aa00ef73.png)

### Modificações no projeto

Nesta seção, abordaremos as modificações propostas para aprimorar o projeto TeaWizard discutidas com os professores orientadores durante as aulas, visando facilitar a experiência do usuário e otimizar o processo de preparação do chá. As seguintes modificações serão incorporadas:

- Reservatório de Água com Sensor de Ultrassom: Uma das modificações fundamentais a ser implementada no projeto é a introdução de um reservatório de água dedicado, equipado com um sensor de ultrassom para medir o volume de água utilizado. A água será colocada em um recipiente com medidas conhecidas, permitindo que o sensor de ultrassom calcule o volume com base na distância entre o sensor e a superfície da água. Essa abordagem proporciona maior precisão na medição do volume de água no tanque, considerando a forma do recipiente e otimizando o processo de preparação do chá.

- Sistema de Bombeamento de Água: Para implementar a nova forma de funcionamento do projeto, será introduzido um sistema de bombeamento de água. A água do reservatório será transferida para um reservatório localizado acima do tanque por meio de uma bomba d'água. Essa configuração permite um controle mais eficiente do fluxo de água, garantindo uma dosagem precisa e facilitando a preparação personalizada do chá.

- Aquecedor de Água e Sensor de Temperatura: Para atingir a temperatura ideal para o preparo do chá, será instalado um dispositivo de aquecimento de água no reservatório superior, juntamente com o sensor de temperatura. Essa combinação permitirá o monitoramento contínuo da temperatura da água durante o processo de aquecimento, garantindo que a temperatura correta seja alcançada antes de prosseguir para as etapas subsequentes.

- Válvula Solenoide para Liberação Controlada: No reservatório de aquecimento, será incorporada uma válvula solenoide que controlará a liberação da água aquecida. Essa válvula solenoide será ativada pelo sistema quando a temperatura desejada for atingida. Dessa forma, o chá será preparado de maneira precisa e automática, proporcionando uma experiência mais conveniente e livre de complicações mecânicas.

Com essas modificações no projeto, espera-se que a experiência do usuário seja significativamente aprimorada. Agora, o usuário pode facilmente preparar a quantidade desejada de chá, basta adicionar a erva no recipiente conectado à saída da válvula solenoide para que o chá seja preparado prontamente. Essas modificações permitem um processo de preparação do chá mais simplificado, eliminando as complexidades mecânicas que existiam na versão anterior do projeto.
