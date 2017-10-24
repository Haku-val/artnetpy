## Python用Artnetモジュール
PythonでArtnetパケットを送れるよう作成したモジュール  
参考元はここ：https://stackoverflow.com/questions/23729886/udp-sockets-in-d-programming-language  
(正直，まだPython経験が乏しいので自信・保証はありません！！)

## 使い方
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

## Artnet module for Python
It is an Artnet module for Python.  
(Artnet is protocol for sending dmx on the ethernet)  
Reference source is here ( https://stackoverflow.com/questions/23729886/udp-sockets-in-d-programming-language )  
(I can't guarantee because Python's experience is not enough.)

## How to use
In the meantime, the sample in the main function in the code is described.  
Put "artnetpy.py" in the same directory. Then,  
```
from artnetpy import Artnet
```  
In this way, import it.

The arguments of the sendDMX method are as follows.
1. Array of DMX signals
2. Destination IP address(IP address of DMX controller)
3. Port number of the controller whose signal you want to output



Finally, the explanation in English was translated by Google translation!! Sory!!
