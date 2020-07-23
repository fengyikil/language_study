对于初学者 java执行工具、javac编译工具；sourcepath、classpath环境变量 ；import关键字 、package关键字 ；java文件、class文件、jar文件这些东西混淆在一起的确很容易晕菜。我也是摸索了挺久，一条条来，说的不对请欢迎指正：

1. java文件通过javac编译工具编译变成 class文件。
2. java执行工具可以执行class文件。 
3. sourcepath定义了源码文件搜索的“根路径”,可以设置多条根路径。
4. classpath定义了class文件搜索的“根路径”,可以设置多条根路径。
5. package关键字指明当前源文件和此文件被编译成class后的文件所在“相对路径”， package和电脑文件系统的目录其实是一个意思，比如 com.xx.yy 对应 Linux的 com/xx/yy 对应windows的com\xx\yy。但是注意一个问题，这个路径是相对的，因为没有根，根需要从sourcepath或classpath里面去找。比如根 classpath = D:\A;D:\B。那么完整的物理路径就可能是 D:\A\com\xx\yy 也可能是 D:\B\com\xx\yy所以同属一个package的源码文件也即开头都用了 package com.xx.yy 的源码文件不一定非要在同一个物理目录下面。
6. javac编译过过程中遇到import语句，就会根据 “classpath + 相对路径”去找 class文件，根据“sourcepath+相对路径“去找源文件。规则是这样的：如果只有class文件，就直接用class文件。如果只有源文件，就把源文件编译成class文件。如果既有class文件又有源文件，就会检查文件修改的时间戳，如果class文件晚于源文件，就直接用class文件，如果早于源文件，就重新编译源文件。另外关于找到的标准要满足两条：文件名必须跟类名一样。文件里面package定义的相对路径必须和import定义的相对路径一样。
7. 简单说一下class文件，前面提到的相对路径信息在源码中是package关键字指明的,class文件中也有这些信息，只不过不是在文件头部指明，而是直接内化成类全称了，看个例子：源码：
 `package A;public class Hello{public static void main(String args[]){System.out.println("Hello World!");}}`
   `class文件 反编译效果：public class A.Hello {public A.Hello();public static void main(java.lang.String[]);}`

8. 注意 Hello类直接变成了 A.Hello,也就是类名称自动包含了路径信息。

9. java执行class文件时，遇到 如new、getstatic 等等需要创建类实例的相关指令时，就会加载相关的class文件（也称动态加载），那么jvm会去哪里找class文件呢？跟javac类似还是通过“classpath + 相对路径”去找。

10. jar文件就是把class文件以及相对目录结构打包而成的文件，感兴趣可以直接解压看看。