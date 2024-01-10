package scanner;

import java.util.Scanner;

public class ScannerWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("문자열을 입력하세요(exit: 종료) :");
            String str = scanner.nextLine();
            if (str.equals("exit")) {
                break;
            }
            System.out.println("입력한 문자열 : " + str);
        }
    }
}
