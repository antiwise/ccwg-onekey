cd wechatgameres
rmdir /s/q res
cd ..
move wechatgame/res wechatgameres
cd wechatgameres
copy spr_giftbaglogo.png res\raw-assets\resources\Texture
copy login.png res\raw-assets\resources\Texture
cd ..
python3 wechatgame-rebuild.py
python3 tinypng.py
cd wechatgameres
"D:\Program Files\7-Zip\7z.exe" a res.zip res
echo �ϴ��������
python3 upload.py
pause