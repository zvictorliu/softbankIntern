 [filter](http://doc.aldebaran.com/2-5/naoqi/peopleperception/alfacedetection.html?highlight=facedetected#temporal-filter)概念，实现检测到只报一次，同时持续检测的功能

https://github.com/zvictorliu/softbankIntern/blob/5fb1c175e5f3a89364603d055b0ac10afbb27c83/src/recoFace.py#L16-L20

意思是`p[1][end]`的这几种情况代表了识别结果

https://github.com/zvictorliu/softbankIntern/blob/5fb1c175e5f3a89364603d055b0ac10afbb27c83/src/recoFace.py#L21

而至于`p[0]`和`p[1][0:end-1]`是啥也不知道

`p[1][end]`长度为1，大概是`[4]`的情况，这种代表不认识（一定时间内没有认出来）：

https://github.com/zvictorliu/softbankIntern/blob/5fb1c175e5f3a89364603d055b0ac10afbb27c83/src/recoFace.py#L22-L25

而如果长度是2，那么就可能是1个或者多个，`p[1][end]`就是认出来的人名的数组

https://github.com/zvictorliu/softbankIntern/blob/5fb1c175e5f3a89364603d055b0ac10afbb27c83/src/recoFace.py#L26-L31

结合[countFace](https://github.com/zvictorliu/softbankIntern/blob/crgCode/notes/countFaces.md)的情况，推测`p[1][0:end-1]`或许也是和检测到每个人相关的信息，而`p[1][end]`则是检测到的人当中识别出的那些