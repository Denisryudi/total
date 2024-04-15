using System;
class Robo
{
    public int VelocidadeAtual { get; set; } = 0;
    public int VelocidadeMaxima { get; }
    public int VelocidadeMinima { get; }

    public Robo(int vmin, int vmax)
    {
        VelocidadeMinima = vmin;
        VelocidadeMaxima = vmax;
        VelocidadeAtual = vmin;
    }

    public void Acelerar()
    {
        if (VelocidadeAtual < VelocidadeMaxima)
        {
            VelocidadeAtual++;
        }
    }

    public void Desacelerar()
    {
        if (VelocidadeAtual > VelocidadeMinima)
        {
            VelocidadeAtual--;
        }
    }
}

class Program
{
    static void Main()
    {
        int vmin = int.Parse(Console.ReadLine());
        int vmax = int.Parse(Console.ReadLine());
        Console.WriteLine($"{vmin} {vmax}");
            
        Robo r1 = new Robo(vmin, vmax);
        string comandos = Console.ReadLine();
        string comandosUpperCase = comandos.ToUpper();
        
        foreach (char comando in comandosUpperCase)
        {
            if (comando == 'A')
            {
                r1.Acelerar();
            }
            else if (comando == 'D')
            {
                r1.Desacelerar();
            }
        }
        Console.WriteLine(r1.VelocidadeAtual);
        
    }
}