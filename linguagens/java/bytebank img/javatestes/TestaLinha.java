
public class TestaLinha {
	public static void main(String[] args) {
		for(int linha = 0; linha < 10; linha++) {
			for(int col = 0; col < 10; col++) {
				if(col > linha) {
					break;
				}
				System.out.print(">");
			}
			System.out.println();
		}
	}

}
