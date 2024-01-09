package cond;

public class MoveRateEx {

    public static void main(String[] args) {
        double rating = 7.1;
        if (rating <= 9) {
            System.out.println("어바웃 타임을 추천합니다");
        }
        if (rating <= 8) {
            System.out.println("토이 스토리를 추천합니다");
        }
        if (rating <= 7) {
            System.out.println("고질라를 추천합니다");
        }
    }
}
