// 1. 주문 번호 생성하기
function placeOrder(menu) {
  // 1. goCook 함수 호출
  // 2. 실패가 없다
  return new Promise((resolve) => {
    setTimeout(() => {
      const orderId = Math.floor(Math.random() * 1000) + 1;
      // 성공했을 때 다음 동작은 goCook 이다 라는 것을
      // 머리속에 알고있는 상태로 코딩을 해야함
      resolve({ orderId, menu })
    }, Math.random() * 2000);
  })
}


// 2. 실제로 주문하기
function cook(order) {
  // 1. 성공, 실패가 정해져있고
  // 2. 성공 시 goDelivery 로 넘어감
  // 3. 실패 시에는 console 출력
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const isCookingSuccessful = Math.random() < 0.8;
      if (isCookingSuccessful) {
        // 요리를 성공했다는 의미
        // 다음에 할 일: 배달
        resolve(order)
      } else {
        reject(`주문 실패: ${order.menu} 요리 실패, 다시 주문해주세요.`);
      }
    }, Math.random() * 2000);
  })
  
}

function deliver(order) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const isDeliverySuccessful = Math.random() < 0.9;
      if (isDeliverySuccessful) {
        resolve(`주문 성공: ${order.menu} 배달 완료!`)
      } else {
        reject(`주문 실패: ${order.menu} 배달 실패, 다시 주문해주세요.`);
      }
    }, Math.random() * 2000);
  })
  
}

// 배달 시작
async function processOrder(orderDetails) {
  // async & await 를 사용한 버전
  // Promise Chaining 의 가독성 문제를 해결하기 위해 등장
  // 일반적으로 try & catch 와 같이 사용을 한다.
  try {
    // await : 비동기 함수의 완료를 기다렸다가,
    // resolve 를 통해 전달된 데이터를 반환한다.
    const returnedOrder = await placeOrder(orderDetails.menu)
    console.log(`주문이 생성되었습니다. ${returnedOrder.menu} 요리 주문 ID: ${returnedOrder.orderId}`);

    const cookedOrder = await cook(returnedOrder)
    console.log(`${cookedOrder.menu} 요리 완료!`);

    const status = await deliver(cookedOrder)
    console.log(status)
    console.log("-----------------------------");

  } catch (error) {
    console.error(error)
  }
}

const orderDetailsList = [
  { menu: "치킨" },
  { menu: "피자" },
  { menu: "샐러드" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});
