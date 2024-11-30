import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { resolve } from 'path';
import { loadEnv } from 'vite';

// 加载环境变量
function getPort(mode, defaultPort = 5173) {
  const env = loadEnv(mode, process.cwd());
  const port = env.VITE_PORT || defaultPort; // 从环境变量中读取端口
  return parseInt(port, 10);
}

export default defineConfig(({ mode }) => {
  const port = getPort(mode, 3000); // 默认端口为 3000

  return {
    base: mode === 'production' ? './' : '/',
    plugins: [vue()],
    root: resolve(__dirname, 'gui'), // 指定根目录为 gui
    build: {
      outDir: resolve(__dirname, 'dist'), // 打包输出到项目根目录的 dist 文件夹
      rollupOptions: {
        input: resolve(__dirname, 'gui/index.html'), // 指定 HTML 入口文件
      },
      assetsDir: 'assets', // assetsDir 指的是 dist 中存放静态资源的目录,即 dist/assets
    },
    resolve: {
      alias: {
        '@': resolve(__dirname, 'gui/src'), // 配置路径别名
      },
    },
    define: {
      'process.env.NODE_ENV': JSON.stringify(mode), // 定义环境变量key=process.env.NODE_ENV的值
    },
    server: {
      open: true, // 自动打开浏览器
      host: 'localhost',
      port, // 使用加载的端口
    },
  };
});
