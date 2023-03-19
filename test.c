#include <stdio.h>
typedef struct T{
    int num;
    struct T *nxt;
}test;
void pop(test *t){
    t=t->nxt;
}
int main(){
    test a,b;
    a.num=1,b.num=2;
    a.nxt=&b;
    pop(&a);
    printf("%d",a.num);
}