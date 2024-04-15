/*using System;

class Program
{
    static void Main()
    {
        // Pergunta ao usuário quantos jogos deseja adicionar:
        Console.Write("Digite a quantidade de jogos: ");
        int quantidadeJogos = int.Parse(Console.ReadLine());

        // TODO: Inicializa os arrays com base na quantidade informada pelo usuário:
       	string[] nomesJogos = new string[quantidadeJogos];

        // TODO: Crie um Loop para adicionar jogos conforme a quantidade especificada:
       	for(int i = 0; i < quantidadeJogos; i++)
		{
        //TODO: Chame a função AdicionarJogo para obter o nome do jogo e armazená-lo no array:
			AdicionarJogo(i, nomesJogos);
		}
		
		

        // Exibe o resumo da adição de jogos
        ExibirResumoAdicaoJogos(quantidadeJogos, nomesJogos);
    }
	
    static void AdicionarJogo(int indice, string[] nomes)
    {
        // Entrada do nome do jogo
		Console.Write($"Digite o nome do jogo {indice + 1}: ");
        nomes[indice] = Console.ReadLine();
    }

    static void ExibirResumoAdicaoJogos(int quantidadeJogos, string[] nomes)
    {
	    string nomesConcatenados = string.Join(", ", nomes);

	    Console.WriteLine($"Foram adicionados '{quantidadeJogos}' jogos: {nomesConcatenados} ao catálogo.");


    } 
}
*/