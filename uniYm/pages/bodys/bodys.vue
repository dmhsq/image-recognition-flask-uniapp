<template>
	<view>
		<view class="content">
			<image class="logo" src="/static/main.jpg"></image>
			<view class="text-area">
				<text class="title">{{title}}</text>
			</view>
		</view>
		<uni-list>
			<uni-list-item title="人体关键点位识别(暂时只支持单人)" showArrow thumb="/static/img/keys.png" thumb-size="base" clickable @click="goSb(1)" />
			<uni-list-item title="人体检测以及属性识别(暂时只支持单人)" showArrow thumb="/static/img/attrs.png" thumb-size="base" clickable @click="goSb(2)" />
			<uni-list-item title="人群流量(图片中的人个数)" showArrow thumb="/static/img/peonum.png" thumb-size="base" clickable @click="goSb(3)" />
			<uni-list-item title="手势识别" showArrow thumb="/static/img/hands.png" thumb-size="base" clickable @click="goSb(4)" />
			<uni-list-item title="人像分割(支持多人)" showArrow thumb="/static/img/qiege.png" thumb-size="base" clickable @click="goSb(5)" />
		</uni-list>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: "人体分析"
			}
		},
		methods: {
			goSb(i) {
				if (i == 1) {
					uni.navigateTo({
						url: '../bodyuse/bodykey/bodykey'
					})
				}
				if (i == 2) {
					uni.navigateTo({
						url: '../bodyuse/bodyattr/bodyattr'
					})
				}
				if (i == 3) {
					uni.navigateTo({
						url: '../bodyuse/bodynum/bodynum'
					})
				}
				if (i == 4) {
					uni.navigateTo({
						url: '../bodyuse/bodygesture/bodygesture'
					})
				}
				if (i == 5) {
					uni.navigateTo({
						url: '../bodyuse/bodyseg/bodyseg'
					})
				}
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 70rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
		border-radius: 200px;
	}

	.text-area {
		margin-bottom: 40rpx;
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>
