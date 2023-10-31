// 1. 주문 번호 생성하기
function placeOrder(menu) {
  setTimeout(() => {
    const orderId = Math.floor(Math.random() * 1000) + 1;
    console.log(`주문이 생성되었습니다. ${menu} 요리 주문 ID: ${orderId}`);
  }, Math.random() * 2000);
}

// 2. 실제로 주문하기
function cook(order) {
  setTimeout(() => {
    const isCookingSuccessful = Math.random() < 0.8;
    if (isCookingSuccessful) {
      return true
    } else {
      console.log(`주문 실패: ${order.menu} 요리 실패, 다시 주문해주세요.`);
      return false
    }
  },  Math.random() * 2000);
}

function deliver(order) {
  setTimeout(() => {
    const isDeliverySuccessful = Math.random() < 0.9;
    if (isDeliverySuccessful) {
      console.log(`주문 성공: ${order.menu} 배달 완료!`);
      return true
    } else {
      console.log(`주문 실패: ${order.menu} 배달 실패, 다시 주문해주세요.`);
      return false
    }
  },  Math.random() * 2000);
}

// 배달 시작
function processOrder(orderDetails) {
	// 1. 주문 번호 생성
  placeOrder(orderDetails.menu)
  cook(orderDetails)
  deliver(orderDetails)
}

const orderDetailsList = [
  { menu: "치킨" },
  { menu: "피자" },
  { menu: "샐러드" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});
