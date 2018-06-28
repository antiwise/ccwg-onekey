import tinify
import os
import os.path

# 帐号注册：https://tinypng.com/developers
tinify.key = "你自己的key"

cwd = os.getcwd()
fromFilePath = os.path.join(cwd, "wechatgameres/res")
toFilePath = os.path.join(cwd, "wechatgameres/res")

print(fromFilePath)
print(toFilePath)

def compress_core(inputFile, outputFile):
	source = tinify.from_file(inputFile)
	source.to_file(outputFile)

for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name) # 解析文件名和文件类型后缀
		if fileSuffix == '.png' or fileSuffix == '.jpg':
			toFullPath = toFilePath + root[len(fromFilePath):]
			toFullName = os.path.join(toFullPath, name)
			print(toFullName)
			if os.path.isdir(toFullPath):
				pass
			else:
				os.mkdir(toFullPath)

			compress_core(toFullName, toFullName)


