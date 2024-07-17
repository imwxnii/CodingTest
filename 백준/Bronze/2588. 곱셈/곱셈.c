#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    
    int r1 = a * (b % 10);
    int r2 = a * (b / 10 % 10);
    int r3 = a * (b / 100);
    
    printf("%d\n", r1);
    printf("%d\n", r2);
    printf("%d\n", r3);
    printf("%d\n", r1 + (r2 * 10) + (r3 * 100));

    return 0;
}
