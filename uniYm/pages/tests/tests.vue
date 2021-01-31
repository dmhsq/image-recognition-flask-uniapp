<template>
	<view>
		 <form>
		 	主题:<input class="uni-input" placeholder="输入主题"  v-model="subject" />
			事件:<input class="uni-input" placeholder="输入事件" v-model="event" />
			原因:<input class="uni-input" placeholder="输入原因" v-model="reason"/>
			<view class="uni-list">
				<view class="uni-list-cell">
					<view class="uni-list-cell-left">
						选择声音
					</view>
					<view class="uni-list-cell-db">
						<picker @change="bindPickerChange" :value="index" :range="array" range-key="name">
							<view class="uni-input">{{array[index].name}}</view>
						</picker>
					</view>
				</view>
			</view>
			<button type="primary" style="width: 70%;margin-left: 15%;" @click="downS()">合成</button>
			<button type="default"  :disabled="isOk" @click="goPlay()" style="width: 70%;margin-left: 15%;">播放</button>
			<progress :percent="progressData" active="active" @activeend="activeend" @change="ssr()" duration="5"></progress>
			<textarea disabled="true" v-model="content"  style="width: 100%;"></textarea>
			
		 </form>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				array: [{name:'女声'},{name: '男声'}, {name:'度逍遥'}, {name:'度丫丫'}],
				index: 0,
				src:"",
				isOk:true,
				progressData:0,
				content:"",
				subject:"",
				event:"",
				reason:"",
				innerAudioContext: uni.createInnerAudioContext(),
				innerAudioContexts: uni.createInnerAudioContext()
			}
		},
		onLoad() {
			
		},
		
		beforeDestroy(){
			this.innerAudioContext.stop()
			this.innerAudioContexts.stop()
		},
		methods: {
			bindPickerChange: function(e) {
				console.log('picker发送选择改变，携带值为：' + e.detail.value)
				this.index = e.detail.value
			},
			activeend(){
				this.isOk = false
			},
			test(){
				let subject = this.subject
				let event = this.event
				let reason = this.reason
				let text =
				        "    哈喽!,小伙伴们大家好，" +
				        subject +
				        event +
				        "是怎么回事呢？" +
				        subject +
				        "相信大家都很熟悉，但是" +
				        subject +
				        event +
				        "是怎么回事呢，下面就让小编带大家一起了解吧。\n    " +
				        subject +
				        event +
				        "，其实就是" +
				        reason +
				        "，大家可能会很惊讶" +
				        subject +
				        "怎么会" +
				        event +
				        "呢？但事实就是这样，小编也感到非常惊讶。\n    这就是关于" +
				        subject +
				        event +
				        "的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！";
				this.content = text;
			},
			goPlay(){
				this.innerAudioContext.src = this.src;
				this.innerAudioContexts.src = '/static/bgm.mp3';
				this.innerAudioContexts.play();
				this.innerAudioContext.play();
			},
			downS(){
				this.isOk = true;
				this.src = "";
				this.progressData = 0;
				this.test();
				let vm = this;
				if(this.content==""){
					uni.showToast({
					    title: '合成内容不得为空',
						icon:'none',
					    duration: 1000
					});
					return ;
				}
				let type = vm.index;
				if(type>=2){
					type++;
				}
				const downloadTask = uni.downloadFile({
					url:'xxxx/voi?result='+vm.content+"&type="+type,
					success:res=>{
						console.log(res)
						vm.src = res.tempFilePath
						
						console.log(res)
					}
				})
				downloadTask.onProgressUpdate((res) => {
				    console.log('下载进度' + res.progress);
					vm.progressData = res.progress;
					setTimeout(function(){
						vm.isOk = false
					},3000)
				    console.log('已经下载的数据长度' + res.totalBytesWritten);
				    console.log('预期需要下载的数据总长度' + res.totalBytesExpectedToWrite);
				});
			}
					
		}
	}
</script>

<style>
.uni-input {
	height: 50rpx;
	padding: 15rpx 25rpx;
	line-height:50rpx;
	font-size:28rpx;
	background:#FFF;
	flex: 1;
}
/* 列表 */
	.uni-list {
		background-color: #FFFFFF;
		position: relative;
		border-top: 0.5px solid black;
		padding-top: 10rpx;
		width: 100%;
		display: flex;
		height: 100rpx;
		flex-direction: column;
	}
	.uni-list-cell {
		position: relative;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}
	.uni-list-cell-left {
	    white-space: nowrap;
		font-size:40rpx;
		padding: 0 30rpx;
	}
	.uni-list-cell-db,
	.uni-list-cell-right {
		flex: 1;
	}
</style>
