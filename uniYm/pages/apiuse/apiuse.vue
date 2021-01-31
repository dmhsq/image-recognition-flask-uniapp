<template>
	<view>
		<view class="content" :class="{bgs:(imgSrc!=''),ybgs:(imgSrc=='')}">
			<image class="logo" :src="imgSrc"></image>
		</view>
		<helang-compress ref="helangCompress"></helang-compress>
		<button type="primary" @click="upfile()" style="width: 70%;margin-left: 15%;">上传图片</button>
		<view class="box" v-if="isHas">
		    <t-table>
		        <t-tr>
		            <t-th>序号</t-th>
		            <t-th>类型</t-th>
		            <t-th>可能性</t-th>
		        </t-tr>
		        <t-tr v-for="(item,index) in tableList" :key="item.name">
		            <t-td>{{ index + 1 }}</t-td>
		            <t-td>{{ item.name }}</t-td>
		            <t-td>{{ item.score | dealVal}}</t-td>
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
	  import helangCompress from '@/components/helang-compress/helang-compress';
	export default {
		components: {
		   tTable,
		   tTh,
		   tTr,
		   tTd,
		   helangCompress
		 }, 
		 filters:{
			 dealVal(val){
				let str = (parseFloat(val)*100 ).toString();
				str = str.substr(0,5)+"%";
				return str;
			 }
		 },
		data() {
			return {
				imgSrc:'',
				type:0,
				tableList:[],
				isHas: false,
				title: ""
			}
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
		onLoad(res) {
			console.log(res.type)
			let title = "";
			this.type=res.type;
			if(res.type==0){
				title = "动物识别"
			}else if(res.type==1){
				title = "菜品识别"
			}else if(res.type==2){
				title = "车辆识别"
			}else if(res.type==3){
				title = "植物识别"
			}else if(res.type==4){
				title = "果蔬识别"
			}else{
				title = "我是你狗哥"
			}
			uni.setNavigationBarTitle({
			    title: title
			});
			this.title = title;
		},
		methods: {
			upfile(){
				let vm = this;
				uni.chooseImage({
				    count: 1,
				    success: function (ress) {
						console.log(ress)
						vm.imgSrc = ress.tempFilePaths[0];
						vm.$refs.helangCompress.compress({
						    src:ress.tempFilePaths[0],
						    maxSize:800,
						    fileType:'jpg',
						    quality:0.85,
						    minSize:-1 //最小压缩尺寸，图片尺寸小于该时值不压缩，非H5平台有效。若需要忽略该设置，可设置为一个极小的值，比如负数。
						}).then(res=>{
							uni.uploadFile({
								//上次测试http://192.168.0.103:8086
								//云端忽略
								//手机调试需要修改ip地址
								//xxxx
								 sizeType: ['compressed'],
								url:'xxxx',
								filePath:res,
								fileType:'image',
								name:'file',
								formData: {
								   'type': vm.type            
								},
								success: (request) => {
									uni.showLoading({
									    title: '加载中'
									});
									if(request.statusCode=='413'){
										console.log('d12dw')
										uni.hideLoading();
										uni.showToast({
										    title: '图片过大,请更换图片再次尝试',
											icon:'none',
										    duration: 1500
										});
										return ;
									}
									console.log(request)
									uni.hideLoading();
									let str =  unescape(request.data.replace(/\\u/g, "%u"));
									let s = JSON.parse(str)
									console.log(str)
									console.log(s.result)
									
									let cl = s.result;
									if(vm.type==1){
										cl.forEach((item,index)=>{
											cl[index].score = item.probability
										})
									}
									vm.tableList = cl;
									uni.hideLoading();
									vm.isHas = true;
									let names = s.result[0].name;
									let historyData = "";
									let date = new Date();
									let year = date.getFullYear();
									let month = date.getMonth() + 1;
									let day = date.getDate();
									let hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
									let minute = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
									let second = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
									month >= 1 && month <= 9 ? (month = "0" + month) : "";
									day >= 0 && day <= 9 ? (day = "0" + day) : "";
									let timer = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second;
									uni.getStorage({
									    key: 'historys',
									    success: function (ress) {
											console.log(ress)
									        let dOne = JSON.parse(ress.data);
											dOne.unshift({date:timer,type:vm.title,onebe:names});
											uni.setStorage({
												key:'historys',
												data: JSON.stringify(dOne)
											})
									    },
										fail:function(){
											let yd = [];
											yd.unshift({date:timer,type:vm.title,onebe:names})
											uni.setStorage({
												key:'historys',
												data: JSON.stringify(yd)
											})	
										}
									});
								}
							})
						})
						
					}
				});
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
		/* height: 400rpx;
		width: 400rpx;
		margin-top: 50rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx; */
	}
	.bgs {
		background-color: #4CD964;
	}
	.ybgs {
		background-color: #C0C0C0;
	}

</style>
