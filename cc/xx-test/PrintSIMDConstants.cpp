/* coding:utf-8
 * Copyright (C) dirlt
 */

#ifdef __x86_64__
#include <nmmintrin.h>
#endif

#define M(x) \
    { #x, x }
struct IMM {
    const char* data;
    int value;

} imm8[] = {

#ifdef __x86_64__
        M(_SIDD_UBYTE_OPS),                // unsigned 8-bit characters
        M(_SIDD_UWORD_OPS),                // unsigned 16-bit characters
        M(_SIDD_SBYTE_OPS),                // signed 8-bit characters
        M(_SIDD_SWORD_OPS),                // signed 16-bit characters
        M(_SIDD_CMP_EQUAL_ANY),            // compare equal any
        M(_SIDD_CMP_RANGES),               // compare ranges
        M(_SIDD_CMP_EQUAL_EACH),           // compare equal each
        M(_SIDD_CMP_EQUAL_ORDERED),        // compare equal ordered
        M(_SIDD_NEGATIVE_POLARITY),        // negate results
        M(_SIDD_MASKED_NEGATIVE_POLARITY), // negate results only before end of string
        M(_SIDD_LEAST_SIGNIFICANT),        // index only: return last significant bit
        M(_SIDD_MOST_SIGNIFICANT),         // index only: return most significant bit
        M(_SIDD_BIT_MASK),                 // mask only: return bit mask
        M(_SIDD_UNIT_MASK),                // mask only: return byte/word mask
#endif
};

#include <cstdio>

using namespace std;

void print_pcmpstr_const() {
    printf("========== pcmpstr constants ==========\n");
    const int n = sizeof(imm8) / sizeof(imm8[0]);
    for (int i = 0; i < n; i++) {
        printf("%s = 0x%02x\n", imm8[i].data, imm8[i].value);
    }
}

int main() {
    print_pcmpstr_const();
    return 0;
}
