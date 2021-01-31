<template>
	<view>
		<view class="content" :class="{bgs:(imgSrc!=''),ybgs:(imgSrc=='')}">
			<image class="logo" :src="imgSrc"></image>
		</view>
		<helang-compress ref="helangCompress"></helang-compress>
		<button type="primary" @click="upfile()" style="width: 70%;margin-left: 15%;">上传图片</button>
		<view class="box" v-if="tableList.length>0">
			<t-table>
				<t-tr>
					<t-th>序号</t-th>
					<t-th>手势</t-th>
					<t-th>可能性</t-th>
				</t-tr>
				<t-tr v-for="(item,index) in tableList" :key="index">
					<t-td>{{index}}</t-td>
					<t-td>{{ item.name}}</t-td>
		            <t-td><t-td>{{ item.probability | dealVal}}</t-td></t-td>
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
		data() {
			return {
				imgSrc: '',
				type: 0,
				tableList: [],
				isHas: false,
				title: ""
			}
		},
		filters:{
			dealVal(val){
				let str = (parseFloat(val)*100 ).toString();
				str = str.substr(0,5)+"%";
				return str;					
			},
			dealXY(val){
				let str = (parseFloat(val)).toString();
				str = str.substr(0,3);
				return str;					
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
		methods: {
			upfile() {
				let vm = this;
				uni.chooseImage({
					count: 1,
					success: function(ress) {
						// 单张压缩
						vm.imgSrc =  ress.tempFilePaths[0]
						vm.$refs.helangCompress.compress({
							src: ress.tempFilePaths[0],
							maxSize: 800,
							fileType: 'jpg',
							quality: 0.85,
							minSize: -1 //最小压缩尺寸，图片尺寸小于该时值不压缩，非H5平台有效。若需要忽略该设置，可设置为一个极小的值，比如负数。
						}).then((res) => {
							console.log(res);
							uni.uploadFile({
								//上次测试http://192.168.0.103:8086
								//云端忽略
								//手机调试需要修改ip地址
								//xxxx/file
								sizeType: ['original'],
								url: 'xxxx/body',
								filePath: res,
								name: 'file',
								formData: {
									'type': 4
								},
								success: (request) => {
									uni.showLoading({
										title: '加载中'
									});
									if (request.statusCode == '413') {
										console.log('sqdqw')
										uni.hideLoading();
										uni.showToast({
											title: '图片过大',
											duration: 1500
										});
										return ;
									}
									console.log(1232)
									console.log(JSON.parse(request.data))
									let sr = JSON.parse(request.data).result
									sr.forEach((item,index)=>{
										let res = item.classname;
										sr[index].name = item.classname
										if(res=="One"||res=="one"){
											sr[index].name = "数字1"
										}else if(res=="Five"||res=="five"){
											sr[index].name = "数字5"
										}else if(res=="Fist"){
											sr[index].name = "拳头"
										}else if(res=="OK"){
											sr[index].name = "OK"
										}else if(res=="Prayer"){
											sr[index].name = "祈祷"
										}else if(res=="Congratulation"){
											sr[index].name = "作揖"
										}else if(res=="Honour"){
											sr[index].name = "作别"
										}else if(res=="Heart_single"){
											sr[index].name = "单手比心"
										}else if(res=="Thumb_up"){
											sr[index].name = "点赞"
										}else if(res=="Thumb_down"){
											sr[index].name = "Diss"
										}else if(res=="ILY"){
											sr[index].name = "Rock"
										}else if(res=="Palm_up"){
											sr[index].name = "掌心向上"
										}else if(res=="Heart_1"){
											sr[index].name = "双手比心"
										}else if(res=="Heart_2"){
											sr[index].name = "双手比心"
										}else if(res=="Heart_3"){
											sr[index].name = "双手比心"
										}else if(res=="two"||res=="Two"){
											sr[index].name = "数字2"
										}else if(res=="three"||res=="Three"){
											sr[index].name = "数字3"
										}else if(res=="four"||res=="Four"){
											sr[index].name = "数字4"
										}else if(res=="six"||res=="Six"){
											sr[index].name = "数字6"
										}else if(res=="seven"||res=="Seven"){
											sr[index].name = "数字7"
										}else if(res=="eight"||res=="Eight"){
											sr[index].name = "数字8"
										}else if(res=="nine"||res=="Nine"){
											sr[index].name = "数字9"
										}else if(res=="Rock"){
											sr[index].name = "Rock"
										}else if(res=="Insult"){
											sr[index].name = "竖中指"
										}else{
											sr[index].name = "其它"
										}
									})
									
									console.log(sr)
									
									if(sr==[]){
										sr = [{"name":"未能识别","score":"奥里给"}];
									}
									
									
									// let str = unescape(request.data.replace(/\\u/g, "%u"));
									// let s = JSON.parse(str)
									// console.log(str.person_info)
									
									vm.tableList = sr;
									// let cl = s.result;
									// vm.tableList = cl;
									uni.hideLoading();

								}
							})
						})
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

	.logo {
		height: 400rpx;
		width: 400rpx;
		margin-top: 50rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.bgs {
		background-color: #4CD964;
	}

	.ybgs {
		background-color: #C0C0C0;
	}
</style>
