## 笔记
---
- __任务一__:配置作业环境

  安装配置docker和tensorflow，由于是在Mac下，所以安装基本上没有什么问题，装完docker，直接查找tensorflow镜像，然后装到本地即可。代码：

  ```
    docker search tensorflow
    docker pull tensorflow/tensorflow
    docker images
    docker run -it -p 8888:8888 tensorflow/tensorflow
  ```
  启动tensorflow以后，浏览器直接访问[http://localhost:8888/](http://localhost:8888/)。
  更多docker run参数设置，参考教程：[Docker 教程](http://www.runoob.com/docker/docker-tutorial.html)

  > 在docker下面装完tensorflow镜像以后，就不用在本地安装[Jupyter notebook](http://jupyter.org/)和[tensorflow](https://www.tensorflow.org/)。每次使用的时候，直接启动docker，就可以使用打包完成的tensorflow镜像。
- __任务二__:语料词频统计

  基本和入学前的任务一致，只是需要做分词。采用jieba分词处理。主要分三个步骤：<br />
  1.  采用正则表达式，匹配出所有中文；
  ```
  re_str = u"([\u4e00-\u9fff]+)"
  re_pattern = re.compile(re_str)
  re_list = re_pattern.findall(my_file)
  ```
  2. 调用jieba分词；
  ```
  result_words = []
  for words in re_list:
      one_word = jieba.lcut(words)
      result_words.extend(one_word)
  ```
  3. 统计词频输出；
  ```
  counter = Counter(result_words).most_common(10)
  print (str(counter).decode("unicode-escape"))
  ```

  > 任务二主要是对词频的统计输出上有些疑问，自己采用的方法有些基础，而且应该是特别大众，主要是对python掌握得不够，对python的标准库以及各种类型了解不多，比如collections、re、pandas、Counter以及python的list、dict类型操作功能。还需要针对性的学习，可是对我来说课程任务驱动的学习，总是很难对一门语言有系统性地掌握，因为总是遇到一个问题需要某一个功能解决的时候，就针对这个功能去学习了，不容易形成体系。
