package casting;

public class Casting4 {

    public static void main(String[] args) {
        int div1 = 3 / 2;
        System.out.println("div1 = " + div1); //1
        double div2 = 3 / 2;
        System.out.println("div2 = " + div2); //1.0
        double div3 = 3.0 / 2;
        System.out.println("div3 = " + div3); //1.5
        double div4 = (double) 3 / 2;
        System.out.println("div4 = " + div4); //1.5
        int a = 3;
        int b = 2;
        double result = (double) a / b;
        System.out.println("result = " + result); //1.5
        //형변환
        //int -> long -> double
        //작은 범위에서 큰 범위로는 대입할 수 있다.
            //이것을 묵시적 형변환 또는 자동 형변환이라 한다.
        //큰 범위에서 작은 범위의 대입은 다음과 같은 문제가 발생할 수 있다. 이때는 명시적 형변환을 사용해야 한다.
            //소수점 버림
            //오버플로우
        //연산과 형변환
            //같은 타입은 같은 결과를 낸다.
            //서로 다른 타입의 계산은 큰 범위로 자동 형변환이 일어난다
    }
}
