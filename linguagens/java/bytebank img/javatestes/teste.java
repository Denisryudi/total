// Usamos o this dentro de um método para acessar um atributo:

class Conta {

        double saldo;
        int numero;
        public Cliente titular;

        void deposita(double valor) {
            this.saldo = this.saldo + valor;
        }

        public char[] getSaldo() {
          return null;
        }

        public char[] saca(int i) {
          return null;
        }
}