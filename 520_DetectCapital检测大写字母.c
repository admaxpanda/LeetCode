#include <string.h>
#include <stdio.h>
int isUpper(char c){
    if(c>='a'&&c<='z')return 0;
    else return 1;
}
int detectCapitalUse(char * word){
    int uppercnt=0,lowercnt=0,first=isUpper(word[0]),len=strlen(word);
    for(int i=0;i<len;i++)
    {
        if(isUpper(word[i]))
            uppercnt++;
        else 
            lowercnt++;
    }
    if(first)
        if(uppercnt==len)
            return 1;
        else if(uppercnt==1)
            return 1;
        else return 0;
    else
        if(lowercnt==len)
            return 1;
        else 
            return 0;
}
int main(){
    printf("%d",detectCapitalUse("QAQ"));
}