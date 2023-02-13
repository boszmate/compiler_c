#include <stdio.h>
int x;

int main(void) {
   printf("Hello Compiler!\n");
   printf("%d\n", 2);
   x = 1;
   x = x + 2;
   if (x > 2) {
      printf("%d\n", x);
   }
   return 0;
}
