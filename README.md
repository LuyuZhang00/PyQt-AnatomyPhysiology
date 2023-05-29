# PyQt_AnatomyPhysiology
---------------------------------

## 1. 功能介绍
这是一个用于解剖生理学选择题随机生成的可独立运行的exe软件，它的功能包括：
- 选择题随机生成
- 判断回答是否正确
- 使用Bing搜索引擎搜索答案

![img_1.png](img%2Fimg_1.png)

![img_2.png](img%2Fimg_2.png)

## 2.文件结构

```
E:.
├─ chromedriver.exe    # chromedriver
├─ main.py          # 主程序
├─ main.spec
│  
├─ README.md        # 说明文档
├─ requirements.txt #项目依赖
├─ test.db          # 数据库文件
├─ windows_ui.py    # UI设计py文件 
├─ windows_ui.ui    # UI设计
│
├─.idea
│
├─build
│  └─main
│
├─dist
│      解剖与生理2随机选择生成器.exe
│      
└─img
```

## 3.主要依赖
- Python == 3.9.13
- PyQt5 == 5.15.9
- Selenium == 4.9.1
- Pyinstaller == 5.10.1
- Sqlite3

