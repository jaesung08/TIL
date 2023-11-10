<template>
<div>
    <button @click="goHome" class="backBtn"> ← 뒤로가기</button>
    <h1>비디오 검색</h1>
    <div class="search-container">
      <input v-model="searchQuery" type="text" placeholder="검색어를 입력하세요" @input="handleInput">
      <button @click="searchVideos">검색</button>
    </div>

    <div v-if="videoEmpty" class="video-container">
      <div v-for="video in videos" :key="video.id.videoId" class="video-card">
        {{ video.id }}
        <div @click="goDetail(video)">
        <img :src="video.snippet.thumbnails.default.url " alt="Thumbnail" class="thumbnail">
        <div class="info-container">
        <h3 class="title">{{ video.snippet.title }}</h3>
        <p class="channel">{{ video.snippet.channelTitle }}</p>
        </div>
        </div>
        <div>
            <button @click="addVideo(video)">나중에 볼 동영상</button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>검색어를 입력해주십시오.</p>
    </div>
</div>

  </template>
  
  <script setup>
import { ref, computed } from 'vue';
import axios from 'axios';
import router from '../router';

const videos = ref([]);
const API_KEY = 'AIzaSyCmTIfBOB-qBwzJ9bXYjBaYIFmec9edIgM'; // Replace with your API key
const youtubeURL = 'https://www.googleapis.com/youtube/v3/search'
const searchQuery = ref('');
const videoEmpty = computed(() => videos.value.length > 0 ? true : false);

const goHome = () => {
  router.push(`/`)
}

const goDetail = (video) => {
    router.push(`/${video.id.videoId}`)
}


const searchVideos = () => {
  // 검색 버튼을 클릭했을 때 호출되는 함수
  // 사용자가 입력한 검색어로 YouTube API를 호출하여 동영상을 검색합니다.
  axios.get(youtubeURL, {
    params: {
      key: API_KEY,
      part: 'snippet',
      type: 'video',
      maxResults: 30,
      q: searchQuery.value,
    },
  })
    .then((response) => {
      videos.value = response.data.items;
    })
    .catch((error) => {
      console.error(error);
    });
};

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
  
  <style scoped>

.backBtn {
        margin: 1rem;
        padding: 1rem 2rem;
        font-size: 1rem;
        border-radius: .5rem;
        outline: none;
        border: none;
    }

/* 검색창 스타일 */
.search-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-container input {
  padding: 5px;
  flex: 1;
}

.search-container button {
  padding: 5px 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  cursor: pointer;
}
  </style>