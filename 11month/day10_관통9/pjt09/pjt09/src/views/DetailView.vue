<template>
    <div>
        <button @click="goHome" class="backBtn"> ← 뒤로가기</button>
        <h1> 상세 페이지 </h1> 
        <div class="container">
            <iframe id="ytplayer" type="text/html" width="640" height="360"
                :src='`https://www.youtube.com/embed/${video.id}`'
                frameborder="0">
            </iframe>
            <div>
            <h1> {{ video.snippet.localized.title }}</h1>
            <strong class="video2"> {{ video.snippet.channelTitle }}</strong>
            <p class="video3">{{ video.snippet.description }}</p>
            </div>
            <div>
                <button @click="addVideo(video)">나중에 볼 동영상</button>
            </div>
        
        </div>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import router from '../router';

const route = useRoute()
const video = ref('')
const videoId = route.params.videoId 
const API_KEY = 'AIzaSyDFkGIj9IAZe2FgRe_D7ryXF-KCv97i0M8'
const googleURL = `https://www.googleapis.com/youtube/v3/videos?part=snippet&key=${API_KEY}&id=${videoId}`

axios.get(googleURL)
    .then((response) => {
        console.log(response.data)
        video.value = response.data.items[0]
    }).catch((error) => {
        console.error(error)
    })

const addVideo = (video) => {
  // 여러 데이터 저장하기
  // 현재 localStorage에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingVideo = JSON.parse(localStorage.getItem('video')) || []

  const isDuplicate = existingVideo.length > 0 && existingVideo.find((item) => item.id === video.id)

  // 중복이 아니라면 추가
  if(!isDuplicate) {
    alert('나중에 볼 동영상에 추가하였습니다.')
    existingVideo.push(video)
  } else{
    alert('이미 추가된 동영상입니다')
    router.push('/later')
  }

  // 수정된 카트 데이터를 localStorage에 저장
  localStorage.setItem('video', JSON.stringify(existingVideo))

}

const goHome = () => {
  router.push(`/`)
}

</script>

<style  scoped>
    .backBtn {
        margin: 1rem;
        padding: 1rem 2rem;
        font-size: 1rem;
        border-radius: .5rem;
        outline: none;
        border: none;
    }

    .container{
        width: 640px;
        margin: 0 auto;

    }
    .video1{
        font-size: xxx-large;
    }
    .video2{
        font-size: x-large;
    }
    .video3{
        font-size: small;
    }
</style>