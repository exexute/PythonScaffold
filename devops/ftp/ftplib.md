<h2>python3</h2>

<h3>类</h3>
FTP、FTP_TLS	

<h3>异常</h3>

ftplib.error_reply、ftplib.error_temp、ftplib.error_perm、ftplib.error_proto

<h3>方法</h3>

FTP.set_debuglevel()
>设置FTP对象的调试等级，默认为0.此设置仅影响标准输出的内容。

FTP.connect()
>连接到给定的主机名、端口，适用于生成FTP对象时不指定主机名。（端口默认为21）
>疑问：能够定义一个FTP对象，尝试多次connnect进行爆破？
>个人理解：connect会阻塞线程；用一个FTP对象通过多线程爆破时，FTP对象就成了临界资源，会影响爆破的速度。
>编码尝试：


FTP.getwelcome()
>功能：获取FTP服务器的欢迎语。(banner)

FTP.login()
>功能：登陆FTP服务器。(不加参数时，默认通过anonymous账户登录)

FTP.abort()
>功能：终止中在进程中的文件传送。此命令不保证可以终止文件的传输

FTP.sendcmd()
>功能：发送执行命令的字符串，返回响应的字符串

FTP.voidcmd()
>功能：发送一个字符串格式的命令，无返回值。如果命令的状态码为：200-299，无任何现象，否则抛出error_reply异常。

>异常：error_perm、>error_temp

>用途：用于维持访问

FTP.retrbinary()
>功能：从FTP服务器下载文件(二进制)

FTP.retrlines()
>功能：从FTP服务器下载文件(文本形式)

FTP.set_pasv()
>功能：设置为被动传送

FTP.storbinary()
>功能：向FTP服务器上传文件(二进制)

FTP.storlines()
>功能：向FTP服务器上传文件(文本形式)

FTP.transfercmd()
>功能：启动与FTP服务器间的数据连接

FTP.ntransfercmd()
>功能：启动与FTP服务器间的数据连接

>返回值：元组(socket, size)。socket:与FTP服务器之间的socket连接、size:文件大小


FTP.mlsd()
>功能：获取FTP服务器的文件详情，可指定多个目录

FTP.nlst()
>功能：获取FTP服务器的文件详情

FTP.dir()
>功能：类似于DIR，无返回值，直接输出值标准输出。

FTP.rename(fromname, toname)
>功能：将fromname重命名为toname

FTP.delete(filename)
>功能：删除filename文件

FTP.cwd(pathname)
>功能：切换目录

FTP.mkd(pathname)
>功能：创建目录

FTP.pwd()
>功能：返回当前所在位置。(str)

FTP.size(filename)
>功能：返回filename的大小。

FTP.quit()
>功能：发送退出命令并关闭与服务器的连接，可能会产生异常。

FTP.close()
>功能：关闭与服务器的连接。不能被用于已经关闭的对象。



[python2]