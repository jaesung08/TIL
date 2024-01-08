package operator;

public class OperatorAdd1 {

    public static void main(String[] args) {
        int a = 0;
        a = a + 1;
        System.out.println("a = " + a);

        a = a + 1;
        System.out.println("a = " + a);

        // 증감 연산자
        ++a;
        System.out.println("a = " + a);
        ++a;
        System.out.println("a = " + a);
        --a;
        System.out.println("a = " + a);
        // 전위 증감 연산자
        int b = 1;
        int c = 0;
        c = ++b;
        System.out.println("c = " + c);
        System.out.println("b = " + b);
        // 후위 증감 연산잔
        c = b++;
        System.out.println("c = " + c);
        System.out.println("b = " + b);
    }
}
