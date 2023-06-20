因为是Choregraphe的代码，因此和本地不太一样，本地需要有这句，后面也需要改：

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L2

这里的`GeneratedClass`不知道是什么：

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L4

后面给`self`添加了多个成员变量：`resolutionMap`（分辨率）, `cameraMap` （哪个摄像头）, `recordFolder`等等：

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L7-L16

这里`Map`就是可选项，box的参数来确定：

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L42-L44



用的还是绝对路径，没有替代符号

`framemanager`, `photoCapture` 都是代理的对象

对异常处理比较专业：

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L26-L30

`onLoad()`，`onUnload()` 方法的执行可以参考[官方解释](http://doc.aldebaran.com/2-5/software/choregraphe/tutos/boxes.html?highlight=onload#how-does-the-set-leds-script-work)，大抵就是整个flow的开始和结束所执行的，至于顺序就不知道了，但对于一个box来说是`init` - `onLoad` - `I/O` - `onUnload`

这行比较重要，不是`os.getcwd()`而是`·ALFrameManager`下的`getBehaviorPath()`

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L37

这句是确保`onLoad`执行过了

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L39-L40

`logger` `time`这些似乎是系统的，不是很理解怎么得到的：

https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L47-L48

最后是设置`photoCapture`的参数，然后`takePicture`：

> https://github.com/zvictorliu/softbankIntern/blob/5c2846954d6fbc6cd97b528ac7b7ae4cd85807fc/src/takePicture.py#L49-L54

这个函数它必须是路径和文件名分开两个参数传入，而且也是绝对路径，不能有特殊符号`.`和`~`，在命令行用`qicli`时也差不多：

```shell
qicli call ALPhotoCapture.takePicture "/home/nao/" "test.jpg"
```

如果是相对路径，，，实话说你都不知道工作目录到底在哪里