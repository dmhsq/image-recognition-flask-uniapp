<template>
	<view>
		<view class="content">
			<image class="logo" src="/static/main.jpg"></image>
			<view class="text-area">
				<text class="title">{{title}}</text>
			</view>
		</view>
		<uni-list>
			 <uni-list-item title="营销号生成器"  showArrow thumb="/static/img/yx.png" thumb-size="base" clickable @click="goSb(0)" />
			 <uni-list-item title="自定义语音合成"  showArrow thumb="/static/img/speech.png" thumb-size="base" clickable @click="goSb(1)" />
			 <uni-list-item title="查看历史"  showArrow thumb="/static/img/laji.png" thumb-size="base" clickable @click="goSb(2)" />
			 <!-- <uni-list-item title="车辆识别"  showArrow thumb="/static/img/car.png" thumb-size="base" clickable @click="goSb(2)" />
			 <uni-list-item title="菜品识别"  file:///C:/Users/11923/Downloads/语音合成(1).pngshowArrow thumb="/static/img/foods.png" thumb-size="base" clickable @click="goSb(1)" />
			 <uni-list-item title="果蔬识别"  showArrow thumb="/static/img/food.png" thumb-size="base" clickable @click="goSb(4)" />
			 <uni-list-item title="清除历史"  showArrow thumb="/static/img/laji.png" thumb-size="base" clickable @click="qclocal()" /> -->
		</uni-list>
	</view>
</template>

<script>
	 
	export default {
		
		data() {
			return {
				title:'狗哥语音合成'
			}
		},
		methods: {
			goSb(i){
				console.log(i)
				if(i==0){
					uni.navigateTo({
						url:'../tests/tests'
					})
				}
				if(i==1){
					uni.navigateTo({
						url:'../viouse/viouse'
					})
				}
				if(i==2){
					uni.navigateTo({
						url:'../voicehost/voicehost'
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

