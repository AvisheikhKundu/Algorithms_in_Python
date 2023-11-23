#include <stdio.h>
#include <stdbool.h>

bool linear_search(int a[], int size, int n) {
    for (int i = 0; i < size; i++) {
        if (a[i] == n) {
            return true;
        }
    }
    return false;
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6};
    int n = 4;
    int size = sizeof(a) / sizeof(a[0]);

    if (linear_search(a, size, n)) {
        printf("Not found\n");
    } else {
        printf("Found\n");
    }

    return 0;
}
