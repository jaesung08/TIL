package array1;

public class ArrayDi1 {

    public static void main(String[] args) {
        // 2x3 2차원 배열, 초기화
        int[][] arr = {
            {1, 2, 3},
            {4, 5, 6}
        };
        // 2차원 배열의 길이를 활용
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                System.out.print(arr[row][column] + " ");
            }
            System.out.println();
        }
    }

}
