这里没有在`onLoad`里面获取模块，而是在`start`里面，对此的解释是防止中途失联

https://github.com/zvictorliu/softbankIntern/blob/fc7b7313b1687149c5cf8009a2edaf2e2514d3ee/src/showImage.py#L44-L46

这里通过建立会话获取服务，而不是通过代理

https://github.com/zvictorliu/softbankIntern/blob/fc7b7313b1687149c5cf8009a2edaf2e2514d3ee/src/showImage.py#L12

然后对于url确实做了区别`http`：

https://github.com/zvictorliu/softbankIntern/blob/fc7b7313b1687149c5cf8009a2edaf2e2514d3ee/src/showImage.py#L33-L35

这段对`url`的处理：

https://github.com/zvictorliu/softbankIntern/blob/fc7b7313b1687149c5cf8009a2edaf2e2514d3ee/src/showImage.py#L19

不太清楚格式要求，涉及到许多东西，反正照这么做吧