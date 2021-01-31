<template>
	<view>
		<view class="content" v-if="tableList.length==0">
			<text class="title">您还没有识别哦~~~</text>
		</view>
		<view class="box" v-if="tableList.length>0">
		    <t-table @change="change">
		        <t-tr>
		            <t-th>时间</t-th>
		            <t-th>类型</t-th>
		            <t-th>最大可能</t-th>
		        </t-tr>
		        <t-tr v-for="item in tableList" :key="item.date">
		            <t-td>{{ item.date }}</t-td>
		            <t-td>{{ item.type }}</t-td>
		            <t-td>{{ item.onebe}}</t-td>
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
		onPullDownRefresh() {
			this.getData();
		},
		onLoad() {
			this.getData();
		},
		onShow() {
			this.getData();
		},
		mounted() {
			// qq.showShareMenu({
			//   showShareItems: ['qq', 'qzone', 'wechatFriends', 'wechatMoment']
			// })
			// wx.showShareMenu({
			//   withShareTicket: true,
			//   menus: ['shareAppMessage', 'shareTimeline']
			// })
		},
		methods: {
			getData(){
				uni.showLoading({
				    title: '加载中'
				});
				let vm = this;
				uni.getStorage({
					key:'historys',
					success: res=>{
						let datas = JSON.parse(res.data);
						uni.hideLoading();
						uni.stopPullDownRefresh();
						vm.tableList = datas;
					},
					fail:function(){
						vm.tableList = [];
						uni.hideLoading();	
						uni.stopPullDownRefresh();
					}
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
.title {
		font-size: 25rpx;
		color: #8f8f94;
	}
</style>
