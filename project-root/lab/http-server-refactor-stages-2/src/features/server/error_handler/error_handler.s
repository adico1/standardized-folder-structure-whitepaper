.include "./src/shared/macros.s"
.include "./src/features/server/shared/constants.s"
.include "./src/features/server/error_handler/messages.s"

.global _handle_setup_socket_error

.text
.align 4

_handle_setup_socket_error:
    mov x12, STACK_SIZE_ERROR_HANDLER
    stack.frame.create x12

    // Print error message
    mov w0, STDOUT
    adrp x1, error_message_setup_socket@PAGE
    add x1, x1, error_message_setup_socket@PAGEOFF
    adrp x2, error_message_setup_socket_len@PAGE
    ldr w2, [x2, error_message_setup_socket_len@PAGEOFF]
    sys.write

    mov w0, #1    ; Return error code
    stack.frame.destroy x12
    ret

.equiv STACK_SIZE_ERROR_HANDLER, 0x10
