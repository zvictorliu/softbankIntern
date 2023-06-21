`session`来自于`qi Framework`，先创建，再连接机器人：

https://github.com/zvictorliu/softbankIntern/blob/979cddab038b5e04287bfba9866dcdae837ff282/src/altabletservice_showimage.py#L42-L44

然后作为对象传入函数执行：

https://github.com/zvictorliu/softbankIntern/blob/979cddab038b5e04287bfba9866dcdae837ff282/src/altabletservice_showimage.py#L49

获取模块的服务：

https://github.com/zvictorliu/softbankIntern/blob/979cddab038b5e04287bfba9866dcdae837ff282/src/altabletservice_showimage.py#L20

使用模块的method：

https://github.com/zvictorliu/softbankIntern/blob/979cddab038b5e04287bfba9866dcdae837ff282/src/altabletservice_showimage.py#L22-L24

对于平板来说，它也有自己的ip，因此这里显示本地图片会有`http://198.18.0.1`的前缀

这种方式是qi framework的，是站在更抽象的角度

其它模块也能用这种方式（已验证）

这种方式也能用ALProxy：

- 在线url可以
- 本地则没有加载出来
- 在机器人身上运行连接失败