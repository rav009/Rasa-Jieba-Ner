# coding=utf-8

import setuptools

setuptools.setup(
    py_modules=["rasa_jieba_ner"],
    name='rasa_jieba_ner',
    version='20210811',
    keywords='rasa, jieba, ner',
    description='A library providers NER for Rasa 2.8 baesd on Jieba',
    author='韦仁杰',
    author_email='603241918@qq.com',
    packages=setuptools.find_packages(),
    python_requires=">=3.4.0",
    install_requires=['jieba', 'rasa']
)
