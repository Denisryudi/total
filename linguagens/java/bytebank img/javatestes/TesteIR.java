public class TesteIR {
    public static void main(String[] args) {
        double salario = 800;

        if (salario >= 1900 && salario <= 2800) {
        	
            double desconto = salario * 0.075;
            System.out.println("O IR é de 7.5% então pode deduzir na declaração o valor de R$" + desconto);
        } else if (salario > 2800 && salario <= 3751) {
        	
            double desconto = salario * 0.15;
            System.out.println("O IR é de 15% e pode deduzir R$" + desconto);
        } else if (salario >= 3751 && salario <= 4664) {
        	
            double desconto = salario * 0.225;
            System.out.println("O IR é de 22.5% e pode deduzir R$" + desconto);
        }
    }
}