包括年龄、性别以及表情都是`ALFaceCharacteristics`模块下面的

这是一个置信因子的设置：

https://github.com/zvictorliu/softbankIntern/blob/4e3520bee5c635f06d018e927584f4df4f7dd5f4/src/getAge.py#L10

这段正是 delay box的核心内容：

https://github.com/zvictorliu/softbankIntern/blob/4e3520bee5c635f06d018e927584f4df4f7dd5f4/src/getAge.py#L25-L31

意思是当设定的定时时间到后就会触发`self.onTimeout`输出，而后面两行是干嘛的就不清楚了

反正就是给了一个检测时间上的限制





要从`ALMemory`里面获取信息，这是比较独特的，存在`PeoplePerception/PeopleList`当中，识别到的每个人都是一个元素：

https://github.com/zvictorliu/softbankIntern/blob/4e3520bee5c635f06d018e927584f4df4f7dd5f4/src/getAge.py#L38-L44

确认是一个人后，还是从`ALMemory`获取相关信息，`PeopleList`数组等于是给了文件夹中人的档案名，返回年龄和置信水平：

https://github.com/zvictorliu/softbankIntern/blob/4e3520bee5c635f06d018e927584f4df4f7dd5f4/src/getAge.py#L45-L52

程序设置了最多识别4个人：

https://github.com/zvictorliu/softbankIntern/blob/4e3520bee5c635f06d018e927584f4df4f7dd5f4/src/getAge.py#L34-L35



