#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <stdbool.h>


//registro
struct Consulta{
	char nome[100];
	int dia;
	int hora;
};

//vari�veis globais
struct Consulta agenda[300];
int qtdAgendamento;


bool verificarDisponibilidade(int diaAgenda, int horaAgenda){   
	
	if(horaAgenda >= 8 && horaAgenda<= 20){
		return true;
	} else {
		printf("Clinica fechada neste hor�rio \n");
		return false;
	}
}

void agendarConsulta(){
	
	int diaAgenda;
	printf("Qual dia do m�s voc� quer agendar? \n");
	fflush(stdin);
	scanf("%d", &diaAgenda);
	
	int horaAgenda;
	printf("Qual hora do dia voc� quer agendar? \n");
	fflush(stdin);
	scanf("%d", &horaAgenda);
	
	if(verificarDisponibilidade(diaAgenda, horaAgenda)){
		printf("Hor�rio dispon�vel \n");
		printf("Vamos confirmar seu agendamento \n");
		agenda[qtdAgendamento].dia = diaAgenda;
		agenda[qtdAgendamento].hora = horaAgenda;
		printf("Qual seu nome? \n");
		fflush(stdin);
		gets(agenda[qtdAgendamento].nome);
		qtdAgendamento = qtdAgendamento + 1;
		printf("Agendamento realizado! \n");
	} else {
		printf("Hor�rio n�o dispon�vel \n");
	}
}

void listarConsulta() {
	int i;
	for(i = 0; i < qtdAgendamento; i++){
		printf("=================\n");
		printf("Nome: %s\n", agenda[i].nome);
		printf("Dia: %d\n", agenda[i].dia);
		printf("Hora: %d\n", agenda[i].hora);
	}
}



void main() {
	
	setlocale(LC_ALL, "");
	
	int opcao;
	qtdAgendamento = 0;
	
	do{
		printf("Deseja uma op��o desejada? \n");
		printf("1 - Agendar \n");
		printf("2 - Listar \n");
		printf("3 - Sair \n");
		fflush(stdin);
		scanf("%d", &opcao);
		
		switch(opcao){
			case 1 :{
				agendarConsulta();
				break;
			}
			case 2 :{
				listarConsulta();
				break;
			}
			case 3 :{
				printf("saindo do programa... \n");
				break;
			}
			default :{
				printf("Op��o inv�lida \n");
				break;
			}		
		}
	}
	while (opcao != 3);
}
