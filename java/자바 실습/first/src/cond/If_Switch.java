package cond;

public class If_Switch {

    public static void main(String[] args) {
        int grade = 2;

        int coupon;
        if (grade == 1) {
            coupon = 1000;
        } else if (grade == 2) {
            coupon = 2000;
        } else if (grade == 3) {
            coupon = 3000;
        } else {
            coupon = 500;
        }
        System.out.println("발급받은 쿠폰 " + coupon);

        int coupon2;
        switch (grade) {
            case 1:
                coupon2 = 1000;
                break;
            case 2:
                coupon2 = 2000;
                break;
            case 3:
                coupon2 = 3000;
                break;
            default:
                coupon2 = 500;
        }
        System.out.println("발급받은 쿠폰2 " + coupon2);
    }
}
