#include <stdio.h>

int main() {
    int kelipatan;
    char simbol;

    scanf("%d %c", &kelipatan, &simbol);

    for (int i = 1; i <= 50; i++) {
        if (i % kelipatan == 0) {
            printf("%c", simbol);
        } else {
            printf("%d", i);
        }

        if (i < 50) {
            printf(" ");
        }
    }
    printf("\n");

    return 0;
}