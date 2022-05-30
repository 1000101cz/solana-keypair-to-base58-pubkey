/* Solana Pubkey Separate
 *    - get wallet public key from solana keypair file
 *
 * usage
 *    - 'gcc main.c -o main'
 *    - './main /path/file_with_keypair'
 *
 * requirements
 *    - python3
 *
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char *keypair_location;
    if (argc>=2) {
        keypair_location = argv[1];
    } else {
        fprintf(stderr,"enter keypair location\n");
    }

    FILE *keypair_file = fopen(keypair_location, "r");
    int private_array[32], public_array[32], keypair_array[64];
    char single_value[3] = {'x'};
    char character;
    int streak = 0;
    int element = 0;
    char *ptr;
    while (!feof(keypair_file)) {
        character = (char)fgetc(keypair_file);
        if (character != '[' && character != ']' && character != ',' && character != ' ') {
            single_value[streak] = character;
            streak++;
        } else {
            if (streak > 0) {
                keypair_array[element] = (int)strtol(single_value,&ptr,10);
                element++;
                streak = 0;
                for (int i = 0; i < 3; i++) {
                    single_value[i] = 'x';
                }
            }
        }
    }

    // separate public and private values
    for (int i = 0; i < 32; i++) {
        private_array[i] = keypair_array[i];
        public_array[i] = keypair_array[i+32];
    }

    // convert int array to hex string
    char public_hex[64] = {'\0'};
    for (int i = 0; i < 32; i++) {
        sprintf(public_hex,"%s%02x",public_hex,public_array[i]);
    }

    // python script to convert hax to base58 string
    char cmd[80];
    sprintf(cmd,"python3 HexTo58.py %s",public_hex);
    printf("public key:\n");
    system(cmd);

    return 0;
}
