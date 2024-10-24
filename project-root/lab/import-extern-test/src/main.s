.global _main
.align 4
.text

_main:
    // Save frame pointer and link register
    stp x29, x30, [sp, #-16]!
    mov x29, sp

    // Call print_hello_world
    bl print_hello_world

    // Exit the program
    mov x0, #0      // Exit status 0
    mov x16, #1     // syscall number for exit
    svc #0x80       // make the syscall

    // We shouldn't reach here, but just in case:
    ldp x29, x30, [sp], #16
    ret

.include "./src/features/public.s"

