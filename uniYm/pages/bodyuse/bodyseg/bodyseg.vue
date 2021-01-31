<template>
	<view>
		<view class="content" ref="imgs" :class="{ybgs:(imgSrc=='')}" :style="{backgroundImage:'url(' + imgBg + ')'}">
			<image class="logo" :src="imgSrc"  ></image>
		</view>
		<helang-compress ref="helangCompress"></helang-compress>
		<button type="primary" @click="upBg()" style="width: 70%;margin-left: 15%;">上传背景图片</button>
		<button type="primary" style="width: 70%;margin-left: 15%;" @click="open()" :style="{backgroundColor:color}" :disabled="imgBg!=''">选择背景颜色</button>
		<button type="primary" @click="upfile()" style="width: 70%;margin-left: 15%;">上传人物图片合成</button>
		<button @click="qkym()" type="warn" style="width: 70%;margin-left: 15%;">清空</button>
		<!-- <t-color-picker ref="colorPickers" :color="color" @confirm="confirm"></t-color-picker> -->
		<t-color-picker ref="colorPickers" @confirm="confirm"></t-color-picker>
		<button type="primary" @click="downF(1)" :disabled="isSave" style="width: 70%;margin-left: 15%;">保存单人物图</button>
		<button type="primary" @click="downF(2)" :disabled="isSave" style="width: 70%;margin-left: 15%;">保存图片</button>
		<view>
			<progress :percent="progressData" active="active"  duration="5" active-mode="forwards" ></progress>
			<button type="default" disabled="true" style="float: right;font-size: 15rpx;margin: 0;border: 0;padding: 0;outline: none;color: #000000;background-color: white;" loading="true" v-if="isJd">{{jd}}</button>
		</view>
		<canvas canvas-id="ones" id="ones" style="width: 100%;" :style="{height:caheight+'px'}"  ></canvas>
		<!-- <view class="box" v-if="tableList.length>0">
			<t-table>
				<t-tr>
					<t-th>类型</t-th>
					<t-th>数量</t-th>
					<t-th>可能性</t-th>
				</t-tr>
				<t-tr v-for="(item,index) in tableList" :key="index">
					<t-td>{{item.type}}</t-td>
					<t-td>{{ item.name}}</t-td>
		            <t-td>{{ item.score}}</t-td>
				</t-tr>
			</t-table>
		</view> -->
	</view>
</template>

<script>
	import tColorPicker from '@/components/t-color-picker/t-color-picker.vue'
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
			helangCompress,
			tColorPicker
		},
		data() {
			return {
				imgSrc: '',
				type: 0,
				tableList: [],
				isHas: false,
				title: "",
				caheight:0,
				isSave:true,
				progressData:0,
				jd:"",
				isJd:false,
				color:'#000000',
				imgBg:'',
				bgheight:0
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
		onLoad(op) {
			let title = '欢迎您回来'
			if(op.text){
				title = "已清空"
			}
			uni.getStorage({
				key:'hasLook',
				success: () => {
					uni.showToast({
					    title: title,
						icon:'none',
					    duration: 1000
					});
				},
				fail:function(){
					uni.showModal({
						title: '提示',
						content: '背景图片和颜色二选一，选择背景图片后，背景色无效'
					})
					uni.setStorage({
						key:'hasLook',
						data:'yes'
					})
				}
			})
			
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
			qkym(){
				uni.redirectTo({
				    url: '../bodyseg/bodyseg?text=已清空'
				});
			},
			upBg(){
				let vm = this;
				uni.chooseImage({
					count:1,
					success:function(ress){
						vm.imgBg=ress.tempFilePaths[0]
						console.log(vm.imgBg)
						let context = uni.createCanvasContext('ones');
						uni.getImageInfo({
							src:vm.imgBg,
							success:function(res){
								let width  =res.width;
								let height = res.height;
								console.log(res)
								uni.getSystemInfo({
									success:function(resq){
										console.log(resq)
										let hh = height;
										height = resq.windowWidth/width*height;
										vm.bgheight = height;
										vm.caheight = height
										context.drawImage(vm.imgBg,0,0,width,hh,0,0,resq.windowWidth,height)
										context.draw()
									}
								})
							}
						})
					}
				})
			},
			 open(item) {
				 console.log(this.$refs)
                // 打开颜色选择器
                this.$refs.colorPickers.open();
            },
            confirm(e) {
                console.log(e)
				this.color = e.hex
            },
			downF(i){
				let vm = this;
				if(i==1){
					uni.saveImageToPhotosAlbum({
						filePath:vm.imgSrc,
						success:function(){
							uni.showToast({
							    title: '保存成功',
								icon:'none',
							    duration: 1500
							});
						}
					})
				}else{
					uni.canvasToTempFilePath({
						canvasId:'ones',
						success:res=>{
							console.log(res.tempFilePath)
							uni.saveImageToPhotosAlbum({
								filePath:res.tempFilePath,
								success:function(){
									uni.showToast({
									    title: '保存成功',
										icon:'none',
									    duration: 1500
									});
								}
							})
						}
					})
				}
				
			},
			upfile() {
				let vm = this;
				
				this.isSave = true
				vm.progressData =0;
				
				
				uni.chooseImage({
					count: 1,
					success: function(ress) {
						vm.jd = "开始"
						vm.isJd = true;
						// 单张压缩
						vm.jd = "压缩图片"
						vm.imgSrc =  ress.tempFilePaths[0]
						vm.$refs.helangCompress.compress({
							src: ress.tempFilePaths[0],
							maxSize: 800,
							fileType: 'jpg',
							quality: 0.85,
							minSize: 400 //最小压缩尺寸，图片尺寸小于该时值不压缩，非H5平台有效。若需要忽略该设置，可设置为一个极小的值，比如负数。
						}).then((res) => {
							vm.jd = "处理图像"
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
									'type': 5
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
									let cawidth = 0;
									let caheight = 0;
									let imwidth = 0;
									let imheight = 0;
									vm.progressData = 20;
									vm.jd = "定位人物"
									uni.downloadFile({
										url:'xxxx/getImg?name='+request.data,
										success:function(resq){
											console.log(resq.tempFilePath)
											vm.imgSrc = resq.tempFilePath
											vm.progressData = 40
											uni.getSystemInfo({
												success:function(res){
													console.log(res)
													vm.jd = "开始绘画"
													cawidth = res.windowWidth
													caheight = res.windowHeight
													uni.getImageInfo({
														src:vm.imgSrc,
														success:function(res){
															console.log(res)
															imwidth=res.width;
															imheight=res.height;
															let height = imwidth/cawidth*imheight
															vm.progressData = 60
															
															
															uni.uploadFile({
																//上次测试http://192.168.0.103:8086
																//云端忽略
																//手机调试需要修改ip地址
																//xxxx/file
																url: 'xxxx/body',
																filePath: vm.imgSrc,
																name: 'file',
																formData: {
																	'type': 2
																},
																success: (request) => {
																	vm.progressData = 80
																	console.log(1232)
																	if(vm.imgBg==''){
																		console.log(JSON.parse(request.data).person_info)
																		let srr = JSON.parse(request.data).person_info;
																		if(srr.length>1){
																			vm.caheight = imheight
																			const context = uni.createCanvasContext('ones')
																			context.setFillStyle(vm.color)
																			context.fillRect(0,0,cawidth,imheight)
																			context.draw()
																			context.drawImage(vm.imgSrc,0,0,imwidth,imheight,0,0,cawidth,imheight)
																			context.draw(true)
																		}else{
																			let sr = [];
																			let ww = 0;
																			let hh = 0;
																			let left = 0;
																			let top = 0;
																			let dx = 0
																			let dy = 0;
																			let ctss = 1;
																			sr = srr[0].location
																			ww = sr.width*ctss;
																			hh = sr.height*ctss;
																			left = sr.left;
																			top = sr.top;
																			dx = cawidth/2 - ww/2
																			dy = 60;	
																			const context = uni.createCanvasContext('ones')
																			vm.caheight = hh+120
																			context.setFillStyle(vm.color)
																			context.fillRect(0,0,cawidth,hh+120)
																			context.draw()
																			context.drawImage(vm.imgSrc,left,top,ww,hh,dx,dy,ww,hh)
																			context.draw(true)
																		}
																		
																		vm.progressData = 100
																		vm.jd = "完成"
																		vm.isJd = false;
																		vm.isSave = false;
																	}else{
																		console.log(JSON.parse(request.data).person_info)
																		let srr = JSON.parse(request.data).person_info;
																		let sr = [];
																		let ww = 0;
																		let hh = 0;
																		let left = 0;
																		let top = 0;
																		let dx = 0
																		let dy = 0;
																		let ctss =0;
																		if(vm.caheight<imheight){
																			ctss = vm.caheight/imheight;
																		}else if(cawidth<imwidth){
																			ctss = cawidth/imwidth;
																		}
																		sr = srr[0].location
																		ww = sr.width;
																		hh = sr.height;
																		left = sr.left;
																		let tops = sr.top
																		let sw = 0;
																		let sh =0;
																		if(vm.caheight<hh){
																			top = sr.top*ctss;
																			sw = ww*ctss;
																			sh = hh*ctss;
																			dx = cawidth/2 - sw/2
																			dy = 0;
																		}else{
																			top = sr.top;
																			sw = ww;
																			sh = hh;
																			dx = cawidth/2 - sw/2
																			dy = 0;
																		}
																		if(srr.length>1){
																			let ones = srr[0].location;
																			let twos = srr[srr.length-1].location
																			left = ones.left;
																			tops = ones.top;
																			ww = twos.left - ones.left + twos.width;
																			hh = ones.height;
																			let sw = ww;
																			let sh = hh;
																			top = sr.top;
																			if(vm.caheight<hh){
																				sw = ww*ctss;
																				sh = hh*ctss;
																				top = sr.top*ctss;
																			}
																			console.log(sw)
																			console.log(sh)
																			console.log(top)
																			dx = cawidth/2 - sw/2
																			const context = uni.createCanvasContext('ones')
																			context.drawImage(vm.imgSrc,0,0,imwidth,imheight,0,0,cawidth,imheight)
																			context.draw(true)
																		}else{
																			const context = uni.createCanvasContext('ones')
																			context.drawImage(vm.imgSrc,left,tops,ww,hh,dx,top,sw,sh)
																			context.draw(true)
																		}
																		
																		
																		
																		vm.progressData = 100
																		vm.jd = "完成"
																		vm.isJd = false;
																		vm.isSave = false;
																		// let sr = JSON.parse(request.data).person_info[0].location;
																		// const context = uni.createCanvasContext('ones')
																		// console.log(sr)
																		// console.log(vm.imgSrc)
																		// console.log(cawidth)
																		// console.log(height)
																		// let left = cawidth-imwidth
																		// context.drawImage(vm.imgSrc,left,0,imwidth,imheight)
																		// context.draw(true)
																		// vm.progressData = 100
																		// vm.jd = "完成"
																		// vm.isJd = false;
																	}
																	// console.log(JSON.parse(request.data).person_info)
																	// let srr = JSON.parse(request.data).person_info;
																	// let sr = [];
																	// let ww = 0;
																	// let hh = 0;
																	// let left = 0;
																	// let top = 0;
																	// let dx = 0
																	// let dy = 0;
																	// let ctss = 1;
																	// if(srr.length==1){
																	// 	sr = srr[0].location
																	// 	ww = sr.width*ctss;
																	// 	hh = sr.height*ctss;
																	// 	left = sr.left;
																	// 	top = sr.top;
																	// 	dx = cawidth/2 - ww/2
																	// 	dy = 60;
																	// }else{
																	// 	sr = srr[0].location
																	// 	console.log(srr.length-1)
																	// 	let srrs = srr[srr.length-1].location
																	// 	console.log(srrs)
																	// 	ww = srrs.left-sr.left+srrs.width;
																	// 	hh = srrs.top-sr.top+srrs.height;
																	// 	ww = ww*ctss
																	// 	left = sr.left;
																	// 	top = sr.top;
																	// 	dx = cawidth/2 - ww/2
																	// 	dy = 60;
																	// }
																	
																	
																	// const context = uni.createCanvasContext('ones')
																	// vm.caheight = hh+120;
																	// vm.isSave = false;
																	// if(vm.imgBg==''){
																	// 	context.setFillStyle('red')
																	// 	context.fillRect(0,0,cawidth,hh+120)
																	// 	context.draw()
																	// 	context.drawImage(vm.imgSrc,left,top,ww,hh,dx,dy,ww,hh)
																	// 	context.draw(true)
																	// }else{
																	// 	let wws = ww;
																	// 	let hhs = hh;
																	// 	vm.caheight = vm.bgheight;
																	// 	hh = vm.caheight-10;
																	// 	hh=hh*ctss
																	// 	ww = hh/vm.caheight*ww;
																	// 	dx = cawidth/2 - ww*ctss/2
																	// 	dy = 5;
																	// 	context.drawImage(vm.imgSrc,left,top,wws,hhs,dx,dy,ww,hh)
																	// 	context.draw(true)
																	// }
																	
																
																	// let cl = s.result;
																	// vm.tableList = cl;
															
																}
															})
															
															
														}
													})
												}
											})
											
										}
									
									})
									
									
									
									
									
									
									// let cc = 400/(uni.upx2px(400)/400);
									// let dx = cawidth/2-imwidth/2;
									// dx = dx/2;
									// let dy = uni.upx2px(60)
									// console.log(vm.$refs)
									// console.log(request.data)
									
									
									// console.log(JSON.parse(request))
									// let sr = JSON.parse(request.data)
									// console.log(sr)
									
									
									
									// let str = unescape(request.data.replace(/\\u/g, "%u"));
									// let s = JSON.parse(str)
									// console.log(str.person_info)
									
									// vm.tableList = ss;
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
		background-size: cover;
	}

	.logo {
		/* height: 400rpx; */
		/* width: 100%; */
	
	}

	.bgs {
		background-image: url(../../../static/img/bgss.jpg);
	}

	.ybgs {
		background-color: #C0C0C0;
	}
</style>
