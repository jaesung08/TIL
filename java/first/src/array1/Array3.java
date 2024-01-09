package array1;

public class Array3 {

    public static void main(String[] args) {
        int[] students; // 배열 변수 선언
        students = new int[]{90, 80, 70, 60, 50}; //배열 생성과 초기화

        // 선언, 생성 초기화를 한번에
        int[] students2 = {90, 80, 70, 60, 50};

        for (int i = 0; i < students.length; i++) {
            System.out.println("학생" + (i + 1) + " 점수: " + students[i]);
        }
    }
}
