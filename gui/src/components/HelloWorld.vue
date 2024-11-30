<template>
  <div class="container">
    <div>
      <div class="hello-world">
        <img src="../assets/vue_logo.png" width="200" height=200 alt="">
        <img src="../assets/add_logo.png" width="200" height=200 alt="">
        <img src="../assets/python_logo.png" width="200" height=200 alt="">
      </div>
    </div>
    <div class="hello-world">
      <p class="description">This is a python + vue framework template, build and package by vite and pyinstaller.</p>
    </div>
    <div class="hello-world">
      <div>
        <h1>{{ count }}</h1>
        <div>
          <el-button class="count-btn" @click="addCount" circle color="#e6e6e6">➕</el-button>
          <el-button color="#d4d4d4"
                     @click="showNotification('hello', 'this is a python + vue framework tempalte', 'success','top-left','300','16')">
            click
          </el-button>
          <el-button color="#d4d4d4"
                     @click="showNotification('hello', 'this is a python + vue framework tempalte', 'success','top-right','300','16')">
            click
          </el-button>
          <el-button class="count-btn" @click="subCount" circle color="#e6e6e6">➖</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js" setup>
import {ref} from 'vue';
import {showNotification} from '@/utils/notification';

const count = ref(0)

const addCount = () => {
  count.value++
}

const subCount = () => {
  count.value--
}

const props = defineProps({})


</script>

<style lang="less" scoped>
.container {
  display: flex;
  //  垂直方向对其
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.hello-world {
  display: flex;
}

.description {
  font-size: 14px;
  color: #afafaf;
}
</style>
 