<template>
  <div>
    <h1>메인페이지</h1>

    <div v-if="vedioEmpty" class="video-container">
      <div v-for="video in videos" :key="video.id.videoId" class="video-card">
        {{ video.id }}
        <div @click="goDetail(video)">
        <img :src="video.snippet.thumbnails.default.url " alt="Thumbnail" class="thumbnail">
        <div class="info-container">
        <h3 class="title">{{ video.snippet.title }}</h3>
        <p class="channel">{{ video.snippet.channelTitle }}</p> 
        </div>
      </div>
      <div >
        <button @click="addVideo(video)">나중에 볼 동영상</button>
      </div>
      </div>
    </div>
    <div v-else>
        로딩중 입니다...
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';
  import router from '../router';

  const videos = ref([])
  const API_KEY = 'AIzaSyCmTIfBOB-qBwzJ9bXYjBaYIFmec9edIgM'
  const API_KEY2 = 'AIzaSyCxm3CA21irzAYv6G_FPIHu973-VjHFZUI'
  // const youtubeURL = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyCmTIfBOB-qBwzJ9bXYjBaYIFmec9edIgM&part=snippet&type=video&q=ssafy'
  // const youtubeURL = 'https://www.googleapis.com/youtube/v3/search?key=' + API_KEY + '&part=snippet&maxResults=30&type=video';
  const youtubeURL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=30&regionCode=kr&key=' + API_KEY ;

  axios.get(youtubeURL)
  .then((response) => {
    // console.log(response.data);
    videos.value = response.data.items
  }) .catch((error) => {
    console.error(error);
  })


  const goDetail = (video) => {
    router.push(`/${video.id}`)
}




  const vedioEmpty = computed(() => {
    return videos.value.length > 0 ? true : false
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



</script>

<style >

.backBtn {
        margin: 1rem;
        padding: 1rem 2rem;
        font-size: 1rem;
        border-radius: .5rem;
        outline: none;
        border: none;
    }

.video-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.video-card {
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 8px;
  width: 300px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.thumbnail {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.info-container {
  margin-top: 10px;
}

.title {
  font-size: 18px;
  margin-bottom: 5px;
}

.channel {
  color: #555;
}

/* Uncomment the following lines if you want to style description and publishedAt */
/*
.description {
  margin-top: 5px;
  color: #888;
}

.published-at {
  color: #888;
}
*/
</style>