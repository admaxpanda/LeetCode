//脑筋急转弯题
#include <string.h>
#include <stdio.h>
int removePalindromeSub(char * s){
    int len=strlen(s);
    for(int i=0;i<len/2;i++)
        if(s[i]!=s[len-i-1])
            return 2;
    return 1;
}
int main(){
    printf("%d",removePalindromeSub("aaba"));
}