package operator;

public class Operator1 {
    public static void main(String[] args) {

        int a = 5;
        int b = 2;
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        int sum = a + b;
        System.out.println("a + b = " + sum);

        int diff = a - b;
        System.out.println("a - b = " + diff);

        int multi = a * b;
        System.out.println("a * b = " + multi);

        int div = a / b;
        // double div2 = a / b;
        System.out.println("a / b = " + div);

        int mod = 5 % 2;
        System.out.println("a % b = " + mod);
    }
}
