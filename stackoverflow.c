#include <stdio.h>
#include <string.h>

void overflow(char *arg){
	//创建缓冲区256个字节
    char buf[256];
    //打印缓冲区起始地址
    printf("ret_addr:%p\n", buf);
    //将程序运行时入的参数复制到缓冲区中
    strcpy(buf, arg);
    //打印缓冲区中的内容
    printf("%s\n", buf);
}

int main(int argc, char *argv[]){
    if(argc==2)
       overflow(argv[1]);
    return 0;
}