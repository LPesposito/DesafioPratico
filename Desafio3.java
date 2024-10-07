public class Desafio3 {
    
    public static void main(String[] args) {
        Integer SOMA = 0;
        Integer K = 1;
        while (K<12) {
            K = K + 1;
            SOMA = K + SOMA;
        }

        System.out.println(SOMA);
    }
}
