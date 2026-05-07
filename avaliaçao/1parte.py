1. Entradas e saídas do sistema
Entradas
Botão de iniciar

Responsável por iniciar o processo.
  
Deve ser lido pelo microcontrolador para detectar o acionamento do operador.

Potenciômetro 1 (tempo de execução)

Valor analógico de 0 a 1023.

Define o tempo de funcionamento do
sistema.

Deve ser convertido para um intervalo entre 1 e 10 segundos.

Potenciômetro 2 (posição do servo)

Valor analógico de 0 a 1023.
Define o ângulo de abertura do servo motor.
Deve ser convertido para um intervalo entre 0° e 180°.


Saídas
Servo motor
Controla a abertura e fechamento da comporta.
Recebe um ângulo como comando
LED vermelho
Indica que o sistema está parado
LED amarelo
Indica que o processo está em execução
LED verde
Indica que o processo foi finalizado.

2. Componentes do sistema e suas funções
ComponenteFunçãoMicrocontrolador (ex.: Arduino)Executa toda a lógica do sistemaBotãoPermite ao operador iniciar o processoPotenciômetro 1Define o tempo de execuçãoPotenciômetro 2Define o ângulo do servoServo motorMovimenta a comportaLED vermelhoIndica sistema paradoLED amareloIndica processo em execuçãoLED verdeIndica processo concluídoResistoresProtegem LEDs e entradasFonte de alimentaçãoFornece energia ao circuito

3. Regras de funcionamento do sistema
Estado inicial

Servo motor na posição inicial (0°).

LED vermelho ligado.

LED amarelo desligado.

LED verde desligado.

Sistema aguardando o botão ser pressionado.

Quando o botão for pressionado
O sistema deve:

Verificar se o processo já está em execução.

Se estiver executando, ignorar o botão.

Isso evita reinício indevido.

Ler o valor do potenciômetro de tempo.

Converter o valor de 0–1023 para 1–10 segundos.

Ler o valor do potenciômetro de posição.

Converter o valor de 0–1023 para 0–180 graus.

Iniciar o processo:

Acender LED amarelo.

Apagar LED vermelho.

Apagar LED verde.

Mover o servo para o ângulo definido.

Manter o servo na posição durante o tempo programado.

Após o tempo:

Retornar servo para 0°.

Apagar LED amarelo.

Acender LED verde.

Indicar processo concluído.

Depois de alguns instantes:

Voltar ao estado inicial.

Acender LED vermelho.

Apagar LED verde.

4. Utilização das estruturas if
As estruturas if serão usadas para tomar decisões no programa.

Exemplo 1 — Verificar botão pressionado
if (botao == PRESSIONADO){    iniciarProcesso();}
Função
Verifica se o operador apertou o botão.

Exemplo 2 — Impedir reinício durante execução
if (processoExecutando == false){    iniciarProcesso();}
Função
Permite iniciar apenas se o sistema estiver parado.
Caso contrário:
if (processoExecutando == true){    // Ignora o botão}

Exemplo 3 — Controle dos LEDs
Sistema parado
if (processoExecutando == false){    digitalWrite(ledVermelho, HIGH);}

Processo em execução
if (processoExecutando == true){    digitalWrite(ledAmarelo, HIGH);}

Exemplo 4 — Finalização do processo
if (tempoAtual >= tempoDefinido){    servo.write(0);    processoExecutando = false;}
Função
Verifica se o tempo terminou para fechar a comporta.

5. Resumo da lógica do sistema
Fluxo geral

Sistema inicia parado.

Operador pressiona botão.

Sistema verifica se já está executando.

Lê os dois potenciômetros.

Define:

tempo de funcionamento;

ângulo do servo.

Servo abre a comporta.

Auarda o tempo programado.

Servo fecha a comporta.

LEDs indicam cada estado.

Sistema volta ao modo de espera.

