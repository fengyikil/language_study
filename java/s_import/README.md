# [基础知识](./base.md)



# 实验一

## 目标

编译单个java文件并运行。

## 步骤：

- 切换到工程目录跟路径
- 编译Test1.java文件：` javac src\cn\dxg\Test1.java` 
- 运行class文件：` java -cp src cn.dxg.Test1`



# 实验二

## 目标

import系统自带库。

## 步骤：

- 切换到工程目录跟路径
- 编译Test2.java文件：` javac src\cn\dxg\Test2.java`
- 运行class文件：`java -cp src cn.dxg.Test2`



# 实验三

## 目标

import第三方库。

## 步骤：

- 切换到工程目录跟路径
- 编译 Test3.java文件：`javac -cp lib\json-20190722.jar src\cn\dxg\Test3.java`
- 运行class文件：`java -cp src;lib\json-20190722.jar cn.dxg.Test3`



# 实验四

## 目标

import自己编写的另外一个类文件。

## 步骤：

- 切换到工程目录跟路径
- 编译 Test4.java文件：`javac -cp src  src\cn\dxg\Test4.java 或 javac -sourcepath src  src\cn\dxg\Test4.java`
- 运行class文件：`java -cp src cn.dxg.Test4`



# 实验五

## 目标

将自己写几个类文件打成jar包库，并调用

## 步骤：

- 切换到工程目录跟路径
- 编译库文件：`javac src\cn\dxg\cal\*.java -d pakage5`
- 打包库文件：`jar -cvf cal.jar -C pakage5 .`
- 编译目标文件：`javac -cp cal.jar src\cn\dxg\Test5.java`
- 执行目标文件: `java -cp cal.jar;src cn.dxg.Test5`



# 实验六

## 目标

将自己写好库文件和main所在文件一起打成jar包，并编写manifest6 文件，指定main方法路径，然后执行jar包

## 步骤：

- 切换到工程目录跟路径

- 编译文件：`javac -cp src src\cn\dxg\Test6.java -d pakage6`

- 编写manifest6文件放在根目录下

```
  Manifest-Version: 1.0         
  Main-Class: cn.dxg.Test6 
      
```

- 打包：`jar -cvfm Test6.jar manifest6 -C pakage6 .`

- 运行：`java -jar Test6.jar`



# 实验七

## 目标

将自己写好库文件和main所在文件一起打成jar包，并编写manifest7文件，指定main方法路径，并指定第三方库路径（和本jar包在同一路径），然后执行jar包

## 步骤：

- 切换到工程目录跟路径
- 编译文件：`javac -cp lib\json-20190722.jar;src src\cn\dxg\Test7.java -d pakage7`
- 编写manifest7文件放在根目录下

```
Manifest-Version: 1.0 
Main-Class: cn.dxg.Test7
Class-Path: json-20190722.jar 

```

- 打包：`jar -cvfm Test7.jar manifest7 -C pakage7 .`

- 运行：因为 manifes中 Class-Path 指定 json-20190722.jar 为当前路径，所以要将此jav包从lib中拷贝出来，保证Test7.jar和json-20190722.jar在同一路径下。

     `java -jar Test7.jar`



# 实验八

## 目标

将自己写好库文件和main所在文件以及json-20190722.jar解压抽取的文件一起打成jar包，并编写manifest8文件，指定main方法路径，然后执行jar包

## 步骤

- 切换到工程目录跟路径
- 编译文件：`javac -cp lib\json-20190722.jar;src src\cn\dxg\Test8.java -d pakage8`
- 编写manifest8文件放在根目录下

```
Manifest-Version: 1.0 
Main-Class: cn.dxg.Test8  

```

- 抽取：解压json-20190722.jar ,复制org目录到pakage8
- 打包：`jar -cvfm Test8.jar manifest8 -C pakage8 .`
- 运行：`java -jar Test8.jar`