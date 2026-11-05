#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    if (a < b) {
        int i = a, j = b;
        while (i <= b && j >= a) {
            printf("%d %d", i, j);
            if (i < b) {
                printf(" - ");
            }
            i++;
            j--;
        }
    } else {
        int i = a, j = b;
        while (i >= b && j <= a) {
            printf("%d %d", i, j);
            if (i > b) {
                printf(" - ");
            }
            i--;
            j++;
        }
    }
    printf("\n");

    return 0;
}