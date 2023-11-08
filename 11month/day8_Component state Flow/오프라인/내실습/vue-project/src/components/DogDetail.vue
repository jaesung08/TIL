<template>
    <div class="dog-box">
        <img :src="dogData.url" alt="Dog Image">
         <div v-if="dogData.detail" class="dog-info">
            <p><strong>품종:</strong> {{ dogData.detail.name }}</p>
            <p><strong>견종 그룹:</strong> {{ dogData.detail.breed_group }}</p>
            <p><strong>높이:</strong> {{ dogData.detail.height.metric }}cm</p>
            <p><strong>무게:</strong> {{ dogData.detail.weight.metric }}kg</p>
            <p><strong>수명:</strong> {{ dogData.detail.life_span }}</p>
            <p><strong>성격:</strong> {{ dogData.detail.temperament }}</p>
        </div>
        <div v-else class="dog-info">
            상세 정보가 없습니다.
        </div>
    </div>

</template>


<script setup>
    const props = defineProps({
      dogData: Object,
    })


</script>
  

<style scoped>
.dog-box {
    border: 1px solid black;
    margin: 10px;
    border-radius: 5px;
    display: flex;
}

.dog-box img {
    width : 200px;
    object-fit: fill;
    border-radius: 5px;
    margin: 5px;
}
.dog-info {
  margin-left: 10px;
}
</style>