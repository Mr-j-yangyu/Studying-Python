##Python3学习记录

####一、环境准备

####### 3.pipenv安装及使用。解决Python版本、项目包依赖的隔离、管理问题  

安装<br>
```
 pip3 install pipenv 
```

进入项目目录，创建虚拟环境<br>
```
 pipenv install [–two||–three]
```

安装其他模块<br>
```
 pipenv install (petl、psutil、requests..)
```
在虚拟环境下运行脚本<br>
```
 pipenv shell 激活虚拟环境 或 pipenv run xxx.py
```
