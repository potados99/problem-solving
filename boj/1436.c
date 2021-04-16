#include <stdio.h>
#include <string.h>
#include <stdbool.h>

static inline bool includes_666(int number) {
    char buf[10] = {0, };
    sprintf(buf, "%d", number);

    return strstr(buf, "666");
}

static inline int search_until_nth(int n) {
    int i = 0;
    int current = 0;

    while (i < n) {
        if (includes_666(++current))
            i++;
    }

    return current;
}

int main() {
    int n; scanf("%d", &n);

    printf("%d\n", search_until_nth(n));
}