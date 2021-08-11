# 介绍
这是一个为Rasa项目实现了中文的实体抽取组件的库。

# 要求
python>=3.4
Rasa=2.8
Jieba=0.42.1

# 使用
1. 安装本library
2. 修改Rasa项目的config文件，使用本library作为实体抽取组件。
## 示例
```
language: zh

pipeline:
    - name: rasa_jieba_ner.JiebaNerExtractor
      part_of_speech: ['nr','m','n']
      dictionary_path: "C:/FR Projects/BI-OLD-DRIVER/rasa-demo/data/user_dict/frcn_corpora.txt"
 ```
其中part_of_speech和dictionary_path是可选参数，分别表示抽取实体的词性和用户字典的路径。

