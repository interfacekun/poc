#include <stdio.h>
#include <string.h>

void overflow(char *arg){
    char buf[256];
    printf("ret_addr:%p\n", buf);
    strcpy(buf, arg);
    printf("%s\n", buf);
}

int main(int argc, char *argv[]){
    if(argc==2)
       overflow(argv[1]);
    return 0;
}