#include <stdio.h>
int main(void){
    int x;
    printf("Hello Compiler!\n");
    printf("%d\n", (int)(2));
    x = 1;
    x = x + 2;
    if (x > 2) {
    printf("%d\n", (int)(x));
        }
    else if (2 < 3) {
        printf("second\n");
    }
    else {
        printf("else statement\n");
    }
    return 0;
}
