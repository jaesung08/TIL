package variable;

public class Var4 {
    public static void main(String[] args) {
        // 정수형 리터럴
        byte b = 127; // -128 ~ 127 (1byte) 잘사용X
        short s = 32767; // -32,768 ~ 32,767 (2byte) 잘사용X
        int i = 2147483647; // 약 20억 (4byte)
        long l = 9223372036854775807L; // 아무튼 제일 큼 (8byte) 끝에 L붙어야함
        // 실수형 리터럴
        float f = 3.3f; // 7자리 정밀도 (4byte) 끝에 f붙여야함 잘사용X
        double d = 6.6666; // 15자리 정밀도
        // L과 F를 붙이는 것은 기본이 int와 double이기 때문에
        // 이를 넘어가면 정해진 알파벳을 붙여서 리터럴을 long 혹은 float으로 지정해준다.
        boolean bo = false; // (1byte)
        char ch = 'C'; // ''를 사용해서 표현 (1byte) 잘사용X
        String str = "문자열 표현"; // ""를 사용해서 표현
        System.out.println(b);
        System.out.println(s);
        System.out.println(i);
        System.out.println(l);
        System.out.println(f);
        System.out.println(d);
        System.out.println(bo);
        System.out.println(ch);
        System.out.println(str);
        // int, long , double, boolean, String 이 자주 사용
        // 클래스는 대문자 시작, 나머지는 소문자로 시작
        // 카멜케이스 잘 지키기
        // 상수는 전부 대문자+언더바(_)로 구분
        // 패키지는 모두 소문자 사용
    }
}
