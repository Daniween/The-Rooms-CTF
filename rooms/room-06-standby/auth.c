#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char password[] = "R3v3rs3_M4st3r";
    if (argc != 2) {
        printf("Usage: ./auth_service <password>\n");
        return 1;
    }

    if (strcmp(argv[1], password) == 0) {
        printf("Accès autorisé. ZIP_PASS = %s\n", password);
    } else {
        printf("Accès refusé.\n");
    }

    return 0;
}
