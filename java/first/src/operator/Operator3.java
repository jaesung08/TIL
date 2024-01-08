package operator;

public class Operator3 {
    public static void main(String[] args) {
        int sum1 = 1 + 2 * 3;
        System.out.println("1 + 2 * 3 = " + sum1);
        int sum2 = (1 + 2) * 3;
        System.out.println("(1 + 2) * 3 = " + sum2);
        // 연산자 우선순위가 애매하거나, 계산이 복잡하다면 무조건 괄호를 쓰자!
    }

}
