
#Definicoes de variaveis
#define led_1 5                                       //pino em que o led 1 ficara
#define led_2 6                                       //pino em que o led 2 ficara

#Declaracao de variaveis
unsigned long tempoAtual;                             # variavel que ira receber o tempo em que o arduino esta ligado em milissegundos. Long armazenam valores maiores que o tipo int e o unsgined significa que estamos desconsiderando valores negativos, fato que aumenta a capacidade de armazenamento do tipo long

long tempoDecorrido = 0;                              //variavel que contara o tempo decorrido para o led 1
long tempoDecorrido2 = 0;                             //variavel que contara o tempo decorrido para o led 2

long tempoLed_1 = 1000;                               //tempo em milissegundos que quero que o led 1 pisque. Pode ser alterado para o tempo que desejar
long tempoLed_2 = 100;                                //tempo em milissegundos que quero que o led 2 pisque. Pode ser alterado para o tempo que desejar

//Condições iniciais do programa
void setup() {
  pinMode(led_1, OUTPUT);                             //seto a porta do led 1 como saida
  pinMode(led_2, OUTPUT);                             //seto a porta do led 2 como saida
}

//Loop 
void loop() {
  tempoAtual = millis();                              //atribuo o tempo (em milissegundos) que o arduino esta ligado na variavel tempoAtual
  efeito1();                                          //chamo a funcao efeito1() que e responsavel pelo piscar do led 1
  efeito2();                                          //chamo a funcao efeito2() que e responsavel pelo piscar do led 2
}


//Construcao da funcao 1 - Funcao que faz o led piscar 1000 milissegundos
void efeito1() {

  if (tempoAtual - tempoDecorrido > tempoLed_1) {     //verifica se passou 1000 milissegundos e se sim
    tempoDecorrido = tempoAtual;                      //subsitui o valor que ja passou pelo tempo atual
    digitalWrite(led_1, !digitalRead(led_1));         //escreve em led_1 o estado inverso em que ele se encontra, ou seja, se esta ligado ele desliga e se estiver desligado o led ligara
  }
}


//Construcao da funcao 2 - Funcao que faz o led piscar 100 milissegundos
void efeito2() { 

  if (tempoAtual - tempoDecorrido2 > tempoLed_2) {    //verifica se passou 100 milissegundos e se sim
    tempoDecorrido2 = tempoAtual;                     //subsitui o valor que ja passou pelo tempo atual
    digitalWrite(led_2, !digitalRead(led_2));         //escreve em led_2 o estado inverso em que ele se encontra, ou seja, se esta ligado ele desliga e se estiver desligado o led ligara
  }
}