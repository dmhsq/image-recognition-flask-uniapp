<template>
	<view>
		<textarea style="width: 100%;" placeholder="请输入合成内容,注意不得超过512个汉字或者(1024个字母),一个字母算半个汉字" v-model="content"></textarea>
		
		<view>当前字数: {{check}} <view style="float: right;"><uni-icons type="close" class="progress-cancel" color="#dd524d" @click="content=''"></uni-icons></view></view>
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
		<button type="primary" @click="downS()" style="width: 70%;margin-left: 15%;">合成</button>
		<button type="primary" @click="downMp()" style="width: 70%;margin-left: 15%;">下载</button> 
		<button type="primary" @click="gohistory()" style="width: 70%;margin-left: 15%;">下载历史</button> 
		<button type="default"  :disabled="isOk"  @click="goPlay()" style="width: 70%;margin-left: 15%;">在线听</button>
		<progress :percent="progressData" active="active" @activeend="activeend" @change="ssr()" duration="5"></progress>
		
		
	</view>
</template>

<script>
	
	export default {
		data() {
			return {
				content:"",
				array: [{name:'女声'},{name: '男声'}, {name:'度逍遥'}, {name:'度丫丫'}],
				index: 0,
				src:"",
				isOk:true,
				progressData:0,
				innerAudioContext:uni.createInnerAudioContext()
				
			}
		},
		computed:{
			check(){
				var str = new String(this.content);  
				var bytesCount = 0;
				for (var i = 0 ,n = str.length; i < n; i++) {  
				    var c = str.charCodeAt(i);  
				    if ((c >= 0x0001 && c <= 0x007e) || (0xff60<=c && c<=0xff9f)) {  
				        bytesCount += 1;  
				    } else {  
				        bytesCount += 2;  
				    }  
				}  
				return bytesCount/2;          
			}
		},
		beforeDestroy() {
			this.innerAudioContext.stop()
		},
		methods: {
			ssr(e){
				console.log(e)
			},
			activeend(){
				this.isOk = false
			},
			showDo(src){
				let vm = this;
				uni.showModal({
				    title: '删除提示',
				    content: '是否删除',
				    success: function (res) {
				        if (res.confirm) {
				            console.log('用户点击确定');
							uni.removeSavedFile({
								filePath: src,
							    success: function () {
									uni.showToast({
										title: '删除成功',
										duration: 1000
									});
									vm.showFile()
							    },
								fail:function(){
									uni.showToast({
									    title: '删除失败',
										icon: 'none',
									    duration: 1000
									});	
								}
							});        
				        } else if (res.cancel) {
				            console.log('用户点击取消');
				        }
				    }
				});
			},
			bindPickerChange: function(e) {
				console.log('picker发送选择改变，携带值为：' + e.detail.value)
				this.index = e.detail.value
			},
			goPlay(){
				this.innerAudioContext.src = this.src;
				this.innerAudioContext.play();
			},
			downMp(){
				let vm = this;
				uni.saveFile({
				      tempFilePath: vm.src,
				      success: function (res) {
				        var savedFilePath = res.savedFilePath;
						vm.src = res.savedFilePath;
						uni.showToast({
						    title: '文件路径为'+savedFilePath,
							icon:'none',
						    duration: 1000
						});
				      },
					  fail:function(){
					  	uni.showToast({
					  	    title: '请勿重复保存，已存在文件'+vm.src,
					  		icon:'none',
					  	    duration: 1000
					  	});
					  }
				    });
			},
			gohistory(){
				uni.navigateTo({
					url:'../voicehost/voicehost'
				})
			},
			downS(){
				this.isOk = true;
				this.src = "";
				this.progressData = 0;
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
 .progress-box {
        display: flex;
        height: 50rpx;
        margin-bottom: 60rpx;
    }
	.uni-icon {
	    line-height: 1.5;
	}
	.progress-cancel {
	    margin-left: 40rpx;
	}
	.uni-padding-wrap{
		/* width:690rpx; */
		padding:0 30rpx;
	}
	.uni-common-mt{
		margin-top:30rpx;
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
	.uni-input {
		height: 50rpx;
		padding: 25rpx 25rpx;
		line-height:50rpx;
		font-size:40rpx;
		background:#FFF;
		flex: 1;
	}
</style>
