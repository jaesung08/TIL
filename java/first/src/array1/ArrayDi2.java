package array1;

public class ArrayDi2 {

    public static void main(String[] args) {
        // 2x3 2차원 배열, 초기화
        int[][] arr = new int[6][6];
        int i = 1;
        // 순서대로 1씩 증가하는 값을 입력한다.
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                arr[row][column] = i++;
            }
        }
        // 2차원 배열의 길이를 활용
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                System.out.print(arr[row][column] + " ");
            }
            System.out.println();
        }

    }
}
