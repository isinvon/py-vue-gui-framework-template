import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router";
// 引入 Element Plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "element-plus/theme-chalk/dark/css-vars.css"; // 引入暗黑主题的 CSS
// 全局样式
import "./styles/index.less";

createApp(App).use(router).use(ElementPlus).mount('#app')
