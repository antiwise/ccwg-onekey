import json

ftp_server = 'https://h5.qiqugame.cn:30013'

lines = []
# 读取game.js
with open('wechatgame/game.js', "r", encoding="utf-8") as file:
	while True:
		line = file.readline()
		if not line:
			break
		lines.append(line)
# 填写远程文件服务器地址
for i in range(len(lines)):
	if 'wxDownloader.REMOTE_SERVER_ROOT' in lines[i]:
		lines[i] = 'wxDownloader.REMOTE_SERVER_ROOT = "%s";\n' % ftp_server
		break

# 重新覆写game.js
with open('wechatgame/game.js', "w", encoding = 'utf-8') as file:
	file.writelines(lines)


lines.clear()
with open('wechatgame/project.config.json', 'r', encoding='utf-8') as file:
	allLines = file.readlines()
	ss = ''.join(allLines)
	jsonObj = json.loads(ss, encoding='utf-8')
	jsonObj['description'] = '项目配置文件。'
	setting = jsonObj['setting']
	setting['urlCheck'] = False
	setting['es6'] = False
	setting['postcss'] = True
	setting['minified'] = False
	setting['newFeature'] = False 
		
	# json.dumps在默认情况下，对于非ascii字符生成的是相对应的字符编码，而非原始字符，只需要ensure_ascii = False
	# sort_keys：是否按照字典排序（a-z）输出，True代表是，False代表否。 
	# indent=4：设置缩进格数，一般由于Linux的习惯，这里会设置为4。 
	# separators：设置分隔符，在dic = {'a': 1, 'b': 2, 'c': 3}这行代码里可以看到冒号和逗号后面都带了个空格，这也是因为Python的默认格式也是如此，
	# 如果不想后面带有空格输出，那就可以设置成separators=(',', ':')，如果想保持原样，可以写成separators=(', ', ': ')。 
	rebuildContent = json.dumps(jsonObj, ensure_ascii = False, sort_keys = False, indent = 4, separators = (',', ' : '))
	print(rebuildContent)
	lines.append(rebuildContent)
	
with open('wechatgame/project.config.json', 'w', encoding='utf-8') as file:
	file.writelines(lines)