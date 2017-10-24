#自作Python用Artnetモジュール
PythonでArtnetパケットを送れるよう作成したモジュール  
参照元はここ：https://stackoverflow.com/questions/23729886/udp-sockets-in-d-programming-language  
(正直，まだPython経験が乏しいので自信・保証はありません！！)

#使い方
artnetpy.py内のmain関数に動作のサンプルを一応記述しています  
artnetpy.pyを同じディレクトリに入れて，  
```
from artnetpy import Artnet
```  
でインポートします．  
sendDMXメソッドの引数は

1. DMX信号の配列
2. 送り先のIPアドレス
3. デコーダの出力ポート番号

となっています．  
使いづらかったりしたら，改造等して構いません．