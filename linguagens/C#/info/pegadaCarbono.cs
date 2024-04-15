using System;
/*
class Program
{
    static void Main()
    {
        // Solicita o nome do usuário, quilômetros percorridos por dia, 
        // Horas de uso de eletrônicos por dia e o número de refeições com carne:
        string nome = Console.ReadLine();
        double quilometrosPorDia = double.Parse(Console.ReadLine());
        int horasDeEletronicos = int.Parse(Console.ReadLine());
        int refeicoesComCarne = int.Parse(Console.ReadLine());

        // Chama o método para calcular a pegada de carbono
        double pegadaDeCarbono = CalcularPegadaDeCarbono(quilometrosPorDia, horasDeEletronicos, refeicoesComCarne);

        // Exibe o resultado para o usuário:
        Console.WriteLine($"{nome}, sua pegada de carbono é de {pegadaDeCarbono} toneladas de CO2 por ano.");

        // Aguarda a entrada do usuário antes de encerrar o programa:
        Console.ReadLine();
    }

    // Crie um método/função para calcular a pegada de carbono com base nos parâmetros fornecidos:
    static double CalcularPegadaDeCarbono(double quilometrosPorDia, int horasDeEletronicos, int refeicoesComCarne)
    {
        double quilometrosDiarios = ((quilometrosPorDia * 365) * 0.2);
        double eletronicosDiarios = horasDeEletronicos * 0.1;
        double carneDiaria = refeicoesComCarne * 0.5;
        double somaTotal = quilometrosDiarios + eletronicosDiarios + carneDiaria;
        
        return somaTotal;
    }
}*/