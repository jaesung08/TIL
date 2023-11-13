const sayT1 = () => {
    console.log('T1이 최고야')
  }
  
  const sayDongHyeon = () => {
    console.log('징동 DOWN!!')
  }
  
  // 다른 파일에서 쓰려면
  // export 키워드로 내보내줘야 한다.
  // export { sayT1, sayDongHyeon }
  
  // 일반 자바스크립트 파일에서는 다음과 같이 작성해야한다.
  // module 객체
  //  - 전역 객체로, js 파일이 모듈 역할을 할 수 있도록 해주는 메타데이터
  // console.log(module)
  module.exports = { sayT1, sayDongHyeon }