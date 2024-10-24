.global main
.align 2

main:
    mov X0, #2                  ; stdout (file descriptor 1)
    adr X1, start_message        ; Load the address of the message
    mov X2, #21                 ; Length of the message
    mov X16, #4                 ; MacOS write syscall
    svc 0                       ; Make the syscall

    mov X0, #0                 ; MacOS exit syscall
    mov X16, #1                  ; Exit code 0
    svc 0                       ; Make the syscall

start_message:    .ascii "Starting Application\n"
