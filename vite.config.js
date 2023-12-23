import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


const HOST = 'http://127.0.0.1:8000/'
// https://vitejs.dev/config/
export default defineConfig({
  build:{
    assetsDir:'static'
  },
  server: {
    port: 8080,
    proxy: {
      "^/api": {
        "target": HOST,
        "ws": true,
        "changeOrigin": true
      },
      "^/media": {
        "target": HOST,
        "ws": true,
        "changeOrigin": true
      },
    }
  },
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
