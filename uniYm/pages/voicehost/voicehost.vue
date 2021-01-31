<template>
	<view>
		<view class="box" v-if="tableList.length>0">
		    <t-table>
		        <t-tr>
		            <t-th>序号</t-th>
		            <t-th>创建时间</t-th>
		            <t-th>操作</t-th>
		        </t-tr>
		        <t-tr v-for="(item,index) in tableList" :key="index">
		            <t-td>{{ index + 1 }}</t-td>
		            <t-td>{{ item.createTime }}</t-td>
		            <t-td><button type="primary" style="font-size: 25rpx;" @click="goPlay(item.filePath)">播放</button><button type="warn" style="font-size: 25rpx;" @click="showDo(item.filePath)">删除</button></t-td>
					
		        </t-tr>
		    </t-table>        
		</view>
	</view>
</template>

<script>
	import tTable from '@/components/t-table/t-table.vue';
	import tTh from '@/components/t-table/t-th.vue';
	import tTr from '@/components/t-table/t-tr.vue';
	import tTd from '@/components/t-table/t-td.vue';  
	export default {
		components: {
		   tTable,
		   tTh,
		   tTr,
		   tTd        
		 }, 
		data() {
			return {
				tableList:[]
			}
		},
		onLoad() {
			this.showFile();
		},
		methods: {
			timeDel(time){
				let date = new Date(time*1000);
				let year = date.getFullYear();
				let month = date.getMonth() + 1;
				let day = date.getDate();
				let hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
				let minute = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
				let second = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
				month >= 1 && month <= 9 ? (month = "0" + month) : "";
				day >= 0 && day <= 9 ? (day = "0" + day) : "";
				let timer = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second;
				return timer;
			},
			showFile(){
				let vm = this;
				uni.getSavedFileList({
				  success: function (res) {
					 console.log(res)
				    let lists = res.fileList;
					lists.forEach((item,index)=>{
						lists[index].createTime = vm.timeDel(item.createTime)
					})
					vm.tableList = lists;
					console.log(vm.tableList)
				  }
				});
			},
			goPlay(src){
				const innerAudioContext = uni.createInnerAudioContext();
				innerAudioContext.src = src;
				innerAudioContext.play();
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
			
		}
	}
</script>

<style>

</style>
