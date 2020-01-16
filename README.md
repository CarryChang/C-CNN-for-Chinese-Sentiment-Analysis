
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)



### C-CNN-for-Chinese-Sentiment-Analysis
#### 一个简单的NLP项目（文本情感分析）的flask后端API，修改了全局model load的方式，增加了模型推理的速度，使用nginx搭配Gunicorn启动Flask，使用虚拟环境搭配sh的启动方式，可以直接对model进行一键重启，并有错误日志监控
 

 
>  支持一键sh部署，flask配置见gun.py，情感分析属于毕业项目整理的一部分（整个项目为顾客意见挖掘）

## 使用方法

> 1. 首先在服务器上部署虚拟环境 ,假设虚拟环境在/home,cd /home 进入home
> 2. 在hoem文件夹中使用python3 -m venv v1创建虚拟环境,v1就是虚拟环境的名字，然后使用souce v1/bin/activate加载虚拟环境
> 4. 在虚拟环境下使用pip install -r requirement.txt 安装所需要的库，然后使用chmod +777 restart.sh部署模型的后端
> 5. 使用ip:8000/predict是post的地址，使用python C-CNN-SA-client.py即可模拟请求，注意模型第一次初始化的时间因为需要加载预训练模型，推理速度有些慢，目前单机单线曾运行的正常推理速度在100ms之内，多进程部署会继续提速


## 代码结构：使用前后分离的结构，完全使用Python实现

> 1. C-CNN-SA-server.py表示后端的model api，直接通过get传参的形式进行，直接搭配nginx+Gunicorn部署即可
> 2. C-CNN-SA-client.py表示模型前端的调用，传入用户的UGC内容，然后使用TextCNN的模型进行识别，模型第一次初始化的时间因为需要加载预训练模型，推理速度有些慢，目前单机单线曾运行的正常推理速度在100ms之内，多进程部署会继续提速


> 后端启动打印的log

<div align=center><img  src="https://github.com/CarryChang/C-CNN-for-Chinese-Sentiment-Analysis/blob/master/pic/api_time_used.png"></div>

> 前端启动打印的结果

<div align=center><img  src="https://github.com/CarryChang/C-CNN-for-Chinese-Sentiment-Analysis/blob/master/pic/restful_api.png"></div>

> Jupyter notebook 打印的结果

<div align=center><img  src="https://github.com/CarryChang/C-CNN-for-Chinese-Sentiment-Analysis/blob/master/pic/result.png"></div>


> 本地Pycharm输出的结果

<div align=center><img  src="https://github.com/CarryChang/C-CNN-for-Chinese-Sentiment-Analysis/blob/master/pic/client.png"></div>


### 基于字符级卷积神经的中文情感分析：
1. 将顾客打分和评论情感进行两极映射，使用数据自动标注和基于弱监督预训练的数据增强方式自动扩充和优化数据集，实验证实了在情感分类中，使用本文的字符级卷积神经网络(C-CNN-SA)可以在不依赖分词的情况下，达到的精度和 F 值均高于词级粒度
2. 在字符级向量化分类模型中，结果显示卷积神经网络在短文本情感分类中效果最好，字符级卷积神经网络在训练速度和效果上优势明显
3. 模型的最后一层改写输出为积极标签的概率，这种输出方式符合情感强度的表达，即输出0.9位这段文字的情感强度，一般大于0.5即视为积极，数字越大，强度越强烈，反则反之，文本分数为0.1的则为消极情感，极性较强

