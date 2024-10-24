.section __TEXT,__text
.global print_message

print_message:
    mov x0, #1                 ; stdout (file descriptor 1)
    mov x8, #64                ; MacOS write syscall
    svc 0                      ; Call the syscall

    cmp x0, #0                 ; Compare return value to 0
    b.ne error_handler         ; If not zero, branch to error_handler
    ret                        ; Return if syscall was successful

error_handler:
    mov x0, #1                 ; Exit with error status code 1
    mov x16, #1                ; MacOS exit syscall
    svc 0                      ; Call the syscall to exit
