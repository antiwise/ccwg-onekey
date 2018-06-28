echo 进入wechatgameres目录
cd wechatgameres
echo 移除res目录
rmdir /s/q res
echo 返回上一层
cd ..
echo 拷贝最近的res到wechatgameres下
move wechatgame/res wechatgameres
echo 进入wechatgameres目录
cd wechatgameres
echo 拷贝登录按钮和分享所需要的图片资源
copy share.png res\raw-assets\resources\Texture
copy login.png res\raw-assets\resources\Texture
echo 退回上一层
cd ..
echo 重构微信配置
python3 wechatgame-rebuild.py
echo 图片资源压缩
python3 tinypng.py
pause