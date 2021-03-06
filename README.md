# 介绍
这是一个为Rasa项目实现了中文的实体抽取组件的库。实体抽取基于Jieba分词的词性识别，可以通过指定词性，将该词性的实体识别出来。
* Rasa: https://github.com/rasahq
* Jieba: https://github.com/fxsjy/jieba

# 要求
* python>=3.4
* Rasa>=2.5
* Jieba>=0.4

# 使用
1. 运行build.cmd中的命令生成wheel包。
3. 使用pip安装wheel包。
3. 修改Rasa项目的config文件，使用本library作为实体抽取组件。
### 示例
```
language: zh

pipeline:
    - name: rasa_jieba_ner.JiebaNerExtractor
      part_of_speech: ['nr','m','n']
      dictionary_path: "C:/data/user_dict/frcn_corpora.txt"
 ```
其中part_of_speech和dictionary_path是可选参数，分别表示抽取实体的词性和用户字典的路径。  
默认情况下，只提取词性为nr的实体，nr即人名。  
注意：windows下用户词典的路径分割符要使用"/"

# 附录：Jieba分词词性列表

### 形容词(1个一类，4个二类)
a 形容词
ad 副形词
an 名形词
ag 形容词性语素
al 形容词性惯用语

### 区别词(1个一类，2个二类)
b 区别词
bl 区别词性惯用语

### 连词(1个一类，1个二类)
c 连词
cc 并列连词

### 副词(1个一类)
d 副词

### 叹词(1个一类)
e 叹词

### 方位词(1个一类)
f 方位词

### 前缀(1个一类)
h 前缀

### 后缀(1个一类)
k 后缀

### 数词(1个一类，1个二类)
m 数词
mq 数量词

### 名词 (1个一类，7个二类，5个三类)
n 名词
nr 人名
nr1 汉语姓氏
nr2 汉语名字
nrj 日语人名
nrf 音译人名
ns 地名
nsf 音译地名
nt 机构团体名
nz 其它专名
nl 名词性惯用语
ng 名词性语素

### 拟声词(1个一类)
o 拟声词

### 介词(1个一类，2个二类)
p 介词
pba 介词“把”
pbei 介词“被”

### 量词(1个一类，2个二类)
q 量词
qv 动量词
qt 时量词

### 代词(1个一类，4个二类，6个三类)
r 代词
rr 人称代词
rz 指示代词
rzt 时间指示代词
rzs 处所指示代词
rzv 谓词性指示代词
ry 疑问代词
ryt 时间疑问代词
rys 处所疑问代词
ryv 谓词性疑问代词
rg 代词性语素

### 处所词(1个一类)
s 处所词

### 时间词(1个一类，1个二类)
t 时间词
tg 时间词性语素

### 助词(1个一类，15个二类)
u 助词
uzhe 着
ule 了 喽
uguo 过
ude1 的 底
ude2 地
ude3 得
usuo 所
udeng 等 等等 云云
uyy 一样 一般 似的 般
udh 的话
uls 来讲 来说 而言 说来
uzhi 之
ulian 连 （“连小学生都会”）

### 动词(1个一类，9个二类)
v 动词
vd 副动词
vn 名动词
vshi 动词“是”
vyou 动词“有”
vf 趋向动词
vx 形式动词
vi 不及物动词（内动词）
vl 动词性惯用语
vg 动词性语素

### 标点符号(1个一类，16个二类)
w 标点符号
wkz 左括号，全角：（ 〔 ［ ｛ 《 【 〖 〈 半角：( [ { <
wky 右括号，全角：） 〕 ］ ｝ 》 】 〗 〉 半角： ) ] { >
wyz 左引号，全角：“ ‘ 『
wyy 右引号，全角：” ’ 』
wj 句号，全角：。
ww 问号，全角：？ 半角：?
wt 叹号，全角：！ 半角：!
wd 逗号，全角：， 半角：,
wf 分号，全角：； 半角： ;
wn 顿号，全角：、
wm 冒号，全角：： 半角： :
ws 省略号，全角：…… …
wp 破折号，全角：—— －－ ——－ 半角：--- ----
wb 百分号千分号，全角：％ ‰ 半角：%
wh 单位符号，全角：￥ ＄ ￡ ° ℃ 半角：$

### 字符串(1个一类，2个二类)
x 字符串
xx 非语素字
xu 网址URL

### 语气词(1个一类)
y 语气词(delete yg)

### 状态词(1个一类)
z 状态词
