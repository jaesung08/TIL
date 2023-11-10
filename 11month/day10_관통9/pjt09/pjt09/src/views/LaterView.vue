<template>
    <div>
        <button @click="goHome" class="backBtn"> ← 뒤로가기</button>
        <h1>나중에 볼 동영상</h1>
        <div v-if="laterVideoEmpty" class="video-container">
            <div v-for="video in laterVideo" :key="video.id" class="video-card">
                <div @click="goDetail(video)">
                <img :src="video.snippet.thumbnails.default.url " alt="Thumbnail" class="thumbnail">
                <div class="info-container">
                <h3 class="title">{{ video.snippet.title }}</h3>
                <p class="channel">{{ video.snippet.channelTitle }}</p>
                </div> 
                </div> 
                <div>
                    <button @click="removeVideo(video)">삭제</button>
                </div>
            </div>
        </div>
        <div v-else>
                <strong>등록된 비디오 없음</strong>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import router from '../router';

const laterVideoEmpty = computed(() => laterVideo.value.length > 0 ? true : false);


const goDetail = (video) => {
    router.push(`/${video.id}`)
}


const laterVideo = ref(null)

laterVideo.value = JSON.parse(localStorage.getItem('video'))


const removeVideo = (video) => {
// 삭제할 아이템 index 검색
const itemIdx = laterVideo.value.findIndex((item) => item.id === video.id )

// 데이터 삭제
laterVideo.value.splice(itemIdx, 1)

// 삭제된 데이터를 기준으로 데이터를 반영
localStorage.setItem('video', JSON.stringify(laterVideo.value))
// laterVideo.value = existingVideo
}


const goHome = () => {
router.push(`/`)
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
</style>