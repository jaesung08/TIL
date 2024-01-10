package loop;

public class Continue {

    public static void main(String[] args) {
        int i = 1; // 3을 생략하는 while문
        while (i <= 5) {
            if (i == 3) {
                i++;
                continue;
            }
            System.out.println(i);
            i++;
        }

    }
}
