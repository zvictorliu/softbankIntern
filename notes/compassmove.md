有fall detection订阅，主要还是这里的move to不太一样

用到`ALVisualCompass`

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/compassmove.py#L5

然后它也有个moveto的method：

https://github.com/zvictorliu/softbankIntern/blob/f3560cce3055f1002358dc56e72f6b8f6703020f/src/compassmove.py#L19

别的就看不到了

------

指令盒上的角度还不是`deg`而是`rad`

![image-20230621144136867](https://cdn.jsdelivr.net/gh/zvictorliu/typoraPics@main/img/image-20230621144136867.png)

差不多就是更安全，更慢的移动了

也因此是先转动