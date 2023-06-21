使用`ALMotion`模块，设置误差范围：

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/moveto.py#L5-L7

移动到设定位置：

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/moveto.py#L26-L28

坐标轴：

![../../_images/axis_def.png](http://doc.aldebaran.com/2-5/_images/axis_def.png)

如果xy同时设置确实是往斜线走，theta是转角，边走边转的，正方向是逆时针

------

通过`almath.Pose2D`将`(x,y,theta)`转换为二维坐标

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/moveto.py#L19-L22

理论终点位置：这里不太理解为什么是这么个关系

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/moveto.py#L23

实际终点位置：

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/moveto.py#L31

检查是否在误差范围内（因为有防护还有什么的会自己停下）

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/moveto.py#L31-L39