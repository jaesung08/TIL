# JS 6일차 정리

## 실생활 예시
- 할로윈을 맞아 파티를 할거야!
  - 치킨, 피자, 족발을 배달앱을 통해 주문하자
- 제약 조건
  - 주문, 요리, 배달 3단계 이루어져있다.
  - 각 단계에서 걸리는 시간은 랜덤
    - `Math.random() * 2000` 활용
  - 주문 함수
    - 랜덤한 주문번호를 생성한다.
  - 요리 함수
    - 20% 확률로 요리가 실패한다.
  - 배달 함수
    - 10% 확률로 배달에 실패한다.

```javascript
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
  }, Math.random() * 2000);
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
  }, Math.random() * 2000);
}

// 배달 시작
function processOrder(orderDetails) {
  placeOrder(orderDetails.menu)
  // cook 의 return 값을 기다리지 않음
  // const flag = cook(orderDetails)
  // console.log(flag)

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

```

- 코드의 문제점
  - return 을 받을 수 없다.
    - 실패 여부를 판단할 수가 없다
  - 순서가 마음대로다.
- 이러한 단점을 callback 함수로 해결 할 수 있다!

```javascript
// 1. 주문 번호 생성하기
function placeOrder(menu, goCook) {
  setTimeout(() => {
    const orderId = Math.floor(Math.random() * 1000) + 1;
    goCook({ orderId, menu })
  }, Math.random() * 2000);
}

// 2. 실제로 주문하기
function cook(order, goDelivery) {
  setTimeout(() => {
    const isCookingSuccessful = Math.random() < 0.8;
    if (isCookingSuccessful) {
      // 요리를 성공했다는 의미
      // 다음에 할 일: 배달
      goDelivery(order)
    } else {
      console.log(`주문 실패: ${order.menu} 요리 실패, 다시 주문해주세요.`);
    }
  }, Math.random() * 2000);
}

function deliver(order, orderComplete) {
  setTimeout(() => {
    const isDeliverySuccessful = Math.random() < 0.9;
    if (isDeliverySuccessful) {
      orderComplete(`주문 성공: ${order.menu} 배달 완료!`)
    } else {
      console.log(`주문 실패: ${order.menu} 배달 실패, 다시 주문해주세요.`);
    }
  }, Math.random() * 2000);
}

// 배달 시작
function processOrder(orderDetails) {
  placeOrder(orderDetails.menu, (order) => {
    console.log(`주문이 생성되었습니다. ${order.menu} 요리 주문 ID: ${order.orderId}`);

    cook(order, (order) => {
      console.log(`${order.menu} 요리 완료!`)

      deliver(order, (status) => {
        console.log(status)
        console.log('-----------------------')
      })
    })
  })
}

const orderDetailsList = [
  { menu: "치킨" },
  { menu: "피자" },
  { menu: "샐러드" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});
```

- 콜백 함수를 사용하면
  - return 없이도 정상적인 흐름 or 비정상적인 흐름을 구성할 수 있음

- 다른 코드들에서는 왜 예제같은 방식을 자주 볼 수 없는가?
  - 콜백 함수가 중첩되어서 가독성이 떨어지고 코드가 복잡해지는 현상(콜백 지옥)이 발생함
  - 콜백 지옥(callback hell)
    - 가독성이 매우 떨어짐
    - 에러 처리가 어려움
    - 순서 보장을 위한 코드 작성이 어렵다

- 해결방법1. Promise

- Promise 기초: 다음에 할 행동을 약속한다!
  - resolve()
    - Promise 객체가 "성공"할 때 호출되어 결과 값을 전달
  - reject()
    - Promise 객체가 "실패"할 때 호출되어 결과 값을 전달
  - then()
    - 로직 이행 성공 시 then 으로 넘어감 (resolve 호출 시)
  - catch()
    - 로직 이행 실패 시 catch 으로 넘어감 (reject 호출 시)

```javascript
const myPromise = new Promise((resolve, reject) => {
    console.log('Promise 생성됨')

    let num = 1
    if (num === 0) {
        resolve('성공')
    } else {
        reject('로직 수행 실패!')
    }
})

myPromise.then((result) => {
    console.log(result)
}).catch((error) => {
    console.log(`error = ${error}`)
})
```

- 아래와 같은 코드는 어떻게 동작할까?

```javascript
const myPromise = new Promise((resolve, reject) => {
    resolve('성공일까?')
    reject('실패일까?')
})

myPromise.then((result) => {
    console.log(result)
}).catch((error) => {
    console.log(`error = ${error}`)
})
```

- [참고] Promise 의 상태
  - Promise는 세가지 상태가 있는데 pending, fulfilled, rejected 상태입니다
    - pending: 대기 상태(아직 아무것도 실행되지 않은 상태)이고
    - resolve 함수가 수행됐을 때 상태가 fulfilled로 바뀌고 .then을 실행합니다.
    - reject 도 같은 방식으로 상태가 rejected로 바뀌고 .catch를 실행합니다.
    - Promise가 한번 상태가 정해지고 나면 pending 상태로 돌아가지 않기 때문에 성공 또는 실패 둘 중에 하나로만 정해집니다.


- 우리 코드에 적용하면 아래와 같다. (4.배달앱_promise.js)

```javascript
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
function processOrder(orderDetails) {
  placeOrder(orderDetails.menu).then((order) => {
    console.log(`주문이 생성되었습니다. ${order.menu} 요리 주문 ID: ${order.orderId}`)
    
    cook(order).then((order) => {
      console.log(`${order.menu} 요리 완료!`)

      deliver(order).then((result) => {
        console.log(result)
      }).catch((error) => {
        console.log(error)
      })
      
    }).catch((error) => {
      console.log(error)
    })
  })
}

const orderDetailsList = [
  { menu: "치킨" },
  { menu: "피자" },
  { menu: "샐러드" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});
```

- 좋은건가...?? 뭔가 이상하다!
  - 콜백 지옥 현상이 그대로 발생한다.
  - 가독성, 중복 제거를 위해 필요한 것이 chaining 기법이다.
  - 5.배달앱_promise_chaining.js

```javascript
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
function processOrder(orderDetails) {
  placeOrder(orderDetails.menu).then((order) => {
    console.log(`주문이 생성되었습니다. ${order.menu} 요리 주문 ID: ${order.orderId}`)
    // cook 함수
    // resolve 나 reject 상태를 가지고 있는 Promise 객체를 반환
    // 해당 객체를 return
    return cook(order)
    // 반환된 Promise 객체에서 호출한 resolve 가 있다면 then 으로 넘어감
  }).then((order) => {
    console.log(`${order.menu} 요리 완료!`);
    return deliver(order)
  }).then((status) => {
    console.log(status)
  }).catch((error) => {
    console.error(error)
  })
}

const orderDetailsList = [
  { menu: "치킨" },
  { menu: "피자" },
  { menu: "샐러드" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});

```

- 해결방법2. Async & Await
  - ES8(ECMAScript 2017) 부터 등장
  - async: 해당 함수가 비동기 함수라는 것을 명시
  - await: 함수 실행 후 결과를 기다리는 키워드

- 6.배달앱_async_await.js

```javascript
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
```


