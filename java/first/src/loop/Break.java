package loop;

public class Break {

    public static void main(String[] args) {
        int sum = 0;
        int i = 1;
        while (true) {
            sum += i;
            System.out.println(sum);
            if (sum > 10) {
                System.out.println("합이 10보다 크면 종료: i=" + i + " sum=" + sum);
                break;
            }
            i++;
        }
    }
}
