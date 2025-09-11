#include <am.h>
#include <nemu.h>

#define KEYDOWN_MASK 0x8000

void __am_input_keybrd(AM_INPUT_KEYBRD_T* kbd) {
    uint32_t code = inl(KBD_ADDR);
    kbd->keydown = code & KEYDOWN_MASK;
    kbd->keycode = code & 0xff;
}
