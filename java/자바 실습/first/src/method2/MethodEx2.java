package method2;

public class MethodEx2 {

    public static void main(String[] args) {
        printMessage("Hello, 1world!", 3);
        printMessage("Hello, 2world!", 5);
        printMessage("Hello, 3world!", 7);
    }

    public static void printMessage(String message, int times) {
        for (int i = 0; i < times; i++) {
            System.out.println(message);
        }
    }
}