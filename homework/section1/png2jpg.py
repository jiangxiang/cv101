def png2jpg(filename, quality_value, save_folder):
	# 不依赖opencv或者pil库，从二进制文件直接解析png文件，并保存成jpeg格式。
	# 其中，jpeg格式的压缩参数由输入指定。
	# 
	# 输入： 
	# 	filename: str, png图像路径
	# 	quality_value: 压缩质量参数
	# 	save_folder: 保存的目标路径
	# 
	# 图像保存文件名：
	#	以学号后两位命名
	# 
	# 返回值:
	#	返回0

