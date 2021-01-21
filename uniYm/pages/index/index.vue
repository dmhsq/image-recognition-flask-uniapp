<template>
	<view>
		<view class="content">
			<image class="logo" src="/static/main.jpg"></image>
			<view class="text-area">
				<text class="title">{{title}}</text>
			</view>
		</view>
		<uni-list>
			 <uni-list-item title="动物识别"  showArrow thumb="/static/img/animal.png" thumb-size="base" clickable @click="goSb(0)" />
			 <uni-list-item title="植物识别"  showArrow thumb="/static/img/botany.png" thumb-size="base" clickable @click="goSb(3)" />
			 <uni-list-item title="车辆识别"  showArrow thumb="/static/img/car.png" thumb-size="base" clickable @click="goSb(2)" />
			 <uni-list-item title="菜品识别"  showArrow thumb="/static/img/foods.png" thumb-size="base" clickable @click="goSb(1)" />
			 <uni-list-item title="果蔬识别"  showArrow thumb="/static/img/food.png" thumb-size="base" clickable @click="goSb(4)" />
			 <uni-list-item title="清除历史"  showArrow thumb="/static/img/laji.png" thumb-size="base" clickable @click="qclocal()" />
		</uni-list>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				title: '狗哥带你图像识别',
				src: ''
			}
		},
		onLoad() {

		},
		methods: {
			qclocal(){
				uni.getStorage({
					key:'historys',
					success:function(){
						uni.showLoading({
						    title: '删除中'
						});
						uni.removeStorage({
						    key: 'historys',
						    success: function () {
								uni.hideLoading();
						       uni.showToast({
						           title: '清除成功',
						           duration: 1500
						       });
						    }
						});
					},
					fail:function(){
						uni.showToast({
							image: '/static/img/tanqi.png',
						    title: '您还没有识别哦',
						    duration: 1500
						});
					}
				})
			},
			goSb(i){
				uni.navigateTo({
					url:'../apiuse/apiuse?type='+i
				})
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
