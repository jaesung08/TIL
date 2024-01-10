package operator;

public class Logical2 {

    public static void main(String[] args) {
        int a = 15;
        // a는 10보다 크고 20보다 작다
        boolean result = a > 10 && a < 20;
        boolean result2 = 10 < a && a < 20;

        System.out.println(result);
        System.out.println(result2);
    }

}
