.global print_bye_world
.align 4
.text

print_bye_world:
    // Save link register
    stp x30, xzr, [sp, #-16]!

    // Load address of hello message
    adr x0, hello_message

    // Calculate string length
    mov x2, #0
count_loop:
    ldrb w1, [x0, x2]
    cbz w1, end_count
    add x2, x2, #1
    b count_loop
end_count:

    // Prepare for write syscall
    mov x16, #4        // syscall number for write
    mov x1, x0         // move string address to x1
    mov x0, #1         // file descriptor 1 is stdout
    svc #0x80          // make the syscall

    // Restore link register and return
    ldp x30, xzr, [sp], #16
    ret

hello_message:
    .asciz "Bye, World!\n"

