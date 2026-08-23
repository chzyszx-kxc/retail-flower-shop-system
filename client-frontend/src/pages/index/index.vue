<template>
  <view class="home-page">

    <!-- hero区沉浸式背景 -->
    <view class="hero-section">
      <view>

        <!-- 主视觉背景 -->
        <image
          class="hero-background"
          src="/static/home/home-hero.png"
          mode="aspectFill"
        ></image>

        <!-- 花礼订购入口 -->
        <view class="hero-action hero-action--order">
          <!-- 花礼订购商店图标 -->
          <image
              class="hero-action-icon hero-action-icon--order"
              src="/static/home/hero-order.png"
              mode="aspectFit"
          ></image>
          <text class="hero-action-title">花礼订购</text>
          <text class="hero-action-subtitle">ORDER</text>
        </view>

        <!-- 花礼定制入口 -->
        <view class="hero-action hero-action--customize">
          <!-- 花礼定制图标 -->
          <image
              class="hero-action-icon hero-action-icon--customize"
              src="/static/home/hero-customize.png"
              mode="aspectFit"
          ></image>
          <text class="hero-action-title">花礼定制</text>
          <text class="hero-action-subtitle">CUSTOMIZE</text>
        </view>
      </view>
    </view>

    <!-- NavigateBar服务入口 -->
    <view class="service-navigation">
      <view class="service-navigation-frame">
        <!-- 积分商城 -->
        <view class="service-item service-item--points">
          <image
              class="service-item-icon service-item-icon--points"
              src="/static/home/service-points.png"
              mode="aspectFit"
          ></image>
          <view class="service-item-label">积分商城</view>
        </view>

        <!-- 预约服务 -->
        <view class="service-item service-item--booking">
          <image
              class="service-item-icon service-item-icon--booking"
              src="/static/home/service-booking.png"
              mode="aspectFit"
          ></image>
          <view class="service-item-label">预约服务</view>
        </view>

        <!-- 会员特权 -->
        <view class="service-item service-item--member">
          <image
              class="service-item-icon service-item-icon--member"
              src="/static/home/service-member.png"
              mode="aspectFit"
          ></image>
          <view class="service-item-label">会员特权</view>
        </view>
      </view>
    </view>

    <!-- 活动展示区域 -->
    <view class="event-banner">
      <image
          src="/static/home/event-banner.png"
          class="event-banner-image"
          mode="widthFix"
      ></image>

      <!-- 这是一个边框 -->
      <view class="event-banner-frame"></view>
    </view>

  </view>
</template>

<script setup lang="ts">

</script>

<style>
.home-page {
  min-height: 100vh;
  background: #f9f9f9;
}

.hero-section {
  position: relative;
  width: 100%;
  height: 1061rpx;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.hero-action {
  position: absolute;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #ffffff;
}

.hero-action--order {
  top: 645rpx;
  left: 67rpx;
  width: 252rpx;
}

.hero-action-icon--order {
  width: 252rpx;
  height: 246rpx;
}

.hero-action--customize {
  top: 685rpx;
  left: 490rpx;
  width: 158rpx;
}

.hero-action-icon--customize {
  width: 137rpx;
  height: 166rpx;
}

.hero-action-title {
  display: block;
  color: #ffffff;
  font-family: "Noto Sans SC", sans-serif;
  font-size: 38rpx;
  font-weight: 700;
  line-height: 40rpx;
  white-space: nowrap;
}

.hero-action--order .hero-action-title {
  margin-top: 8rpx;
}

.hero-action--customize .hero-action-title {
  margin-top: 48rpx;
}


.hero-action-subtitle {
  display: block;
  margin-top: 15rpx;
  color: #ffffff;
  font-family: "Noto Sans SC", sans-serif;
  font-size: 23rpx;
  font-weight: 400;
  line-height: 27rpx;
  white-space: nowrap;
}

.service-navigation {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 170rpx;
  margin-top: -29rpx;
  background: linear-gradient(
      180deg,
      rgba(22, 30, 26, 0.1) 2%,
      #161e1a 14%
  );
}

.service-navigation-frame {
  display: flex;
  align-items: flex-end;
  box-sizing: border-box;
  width: 708rpx;
  height: 158rpx;
  margin: 0 auto;
  padding: 8rpx 57rpx;
  gap: 114rpx;
  border: 0.01px solid #E5E5EA;
  background:
      linear-gradient(
          180deg,
          rgba(22, 30, 26, 0.01) 25%,
          #030303 100%
      ),
      linear-gradient(
          180deg,
          rgba(22, 30, 26, 0.05) 0%,
          #161e1a 32%
      );
}

.service-item {
  display: flex;
  flex-shrink: 0;
  flex-direction: column;
  align-items: center;
}

.service-item--points {
  width: 114rpx;
  height: 143rpx;
}

.service-item--booking {
  width: 107rpx;
  height: 130rpx;
  transform: translateX(11rpx);
}

.service-item--member {
  width: 99rpx;
  height: 128rpx;
}

/* 去掉 image 可能产生的行内空隙，并禁止图标被 Flex 压缩。 */
.service-item-icon {
  display: block;
  flex-shrink: 0;
}

.service-item-icon--points {
  width: 114rpx;
  height: 114rpx;
}

.service-item-icon--booking {
  width: 107rpx;
  height: 99rpx;
  margin-top: -4rpx;
  margin-bottom: 6rpx;
}

.service-item-icon--member {
  width: 111rpx;
  height: 111rpx;
  margin-top: -11rpx;
  margin-bottom: -1rpx;
}

.service-item-label {
  color: #ffffff;
  font-family: Inter, sans-serif;
  font-size: 23rpx;
  font-weight: 400;
  line-height: 29rpx;
  text-align: center;
  white-space: nowrap;
}

.event-banner {
  position: relative;
  z-index: 3;
  width: 100%;
  height: 266rpx;
  margin-top: -1rpx;
  overflow: hidden;
  background: #161e1a;
}

.event-banner-image {
  display: block;
  width: 100%;
}

.event-banner-frame {
  position: absolute;
  top: 0;
  left: 50%;
  box-sizing: border-box;
  width: 708rpx;
  height: 254rpx;
  border: 0.01px solid #E5E5EA;
  transform: translateX(-50%);
}

</style>
