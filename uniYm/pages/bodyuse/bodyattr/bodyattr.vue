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
					<t-th>类型</t-th>
					<t-th>结果</t-th>
					<t-th>可能性</t-th>
				</t-tr>
				<t-tr v-for="(item,index) in tableList" :key="index">
					<t-td>{{item.type}}</t-td>
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
									'type': 2
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
									console.log(JSON.parse(request.data).person_info)
									let sr = JSON.parse(request.data).person_info[0].attributes
									console.log(sr)
									let ss = [];
									sr.orientation.type = "身体朝向";
									sr.gender.type = "性别";
									sr.age.type = "年龄阶段";
									sr.lower_wear.type = "下身服饰";
									sr.upper_wear.type = "上身服饰";
									sr.headwear.type = "是否戴帽子";
									sr.face_mask.type = "是否戴口罩";
									sr.glasses.type = "是否戴眼镜";
									sr.upper_color.type = "上身服饰颜色";
									sr.lower_color.type = "下身服饰颜色";
									sr.cellphone.type = "是否使用手机";
									sr.upper_wear_fg.type = "上身服饰细分类";
									sr.upper_wear_texture.type = "上身服饰纹理";
									sr.umbrella.type = "是否撑伞";
									sr.bag.type = "背包";
									sr.smoke.type = "是否吸烟";
									sr.vehicle.type = "交通工具";
									sr.carrying_item.type = "是否有手提物";
									sr.upper_cut.type = "上方截断";
									sr.lower_cut.type = "下方截断";
									sr.occlusion.type = "遮挡";
									sr.is_human.type = "是否正常人体";
									ss.push(sr.orientation)
									ss.push(sr.gender)
									ss.push(sr.umbrella)
									ss.push(sr.lower_color)
									ss.push(sr.face_mask)
									ss.push(sr.smoke)
									ss.push(sr.bag)
									ss.push(sr.upper_wear)
									ss.push(sr.is_human)
									ss.push(sr.vehicle)
									ss.push(sr.glasses)
									ss.push(sr.headwear)
									ss.push(sr.upper_wear_fg)
									ss.push(sr.upper_wear_texture)
									ss.push(sr.upper_cut)
									ss.push(sr.occlusion)
									ss.push(sr.lower_cut)
									ss.push(sr.cellphone)
									ss.push(sr.carrying_item)
									ss.push(sr.age)
									ss.push(sr.lower_wear)
									ss.push(sr.upper_color)
									// let str = unescape(request.data.replace(/\\u/g, "%u"));
									// let s = JSON.parse(str)
									// console.log(str.person_info)
									console.log(ss[0].score)
									vm.tableList = ss;
									// let cl = s.result;
									// vm.tableList = cl;
									uni.hideLoading();

								}
							})
						})
					}
				})

			},
			upfiles() {
				let vm = this;
				uni.chooseImage({
					count: 1,
					success: function(ress) {
						console.log(ress)
						vm.imgSrc = ress.tempFilePaths[0];
						console.log(JSON.stringify(ress.tempFilePaths));
						uni.compressImage({
							src: ress.tempFilePaths[0],
							width: 'auto',
							height: '10%',
							quality: 10,
							success: res => {
								console.log(res.tempFilePath)


							}

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
