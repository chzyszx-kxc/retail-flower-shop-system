<script setup lang="ts">
import { onLaunch, onShow, onHide } from "@dcloudio/uni-app";
onLaunch(() => {
  console.log("App Launch");
});
onShow(() => {
  console.log("App Show");
});
onHide(() => {
  console.log("App Hide");
});
</script>
<style>
/* #ifdef H5 */
html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: hidden;
  background-color: #eeeeee;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 桌面浏览器中的手机尺寸应用主体 */
#app {
  position: relative;
  width: min(393px, 100vw);
  height: min(852px, 100vh);
  overflow-x: hidden;
  overflow-y: auto;
  scrollbar-width: none;
  background-color: #f9f9f9;
}

#app::-webkit-scrollbar {
  display: none;
}

/* TabBar 固定在手机视口底部 */
.uni-tabbar {
  bottom: max(0px, calc((100vh - 852px) / 2)) !important;
  left: 50% !important;
  width: min(393px, 100vw) !important;
  transform: translateX(-50%) !important;
}
/* #endif */
</style>
