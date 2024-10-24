.include "./src/shared/macros.s"
.include "./src/features/server/shared/constants.s"
.include "./src/features/server/socket/setup_socket_macro.s"

.global _setup_socket

.data
message_listen: .string "Listening for connections\n\n"
.align 4
message_listen_len: .word . - message_listen

.text
.align 4

_setup_socket:
    mov x12, STACK_SIZE_SETUP_SOCKET
    stack.frame.create x12

    create_socket

    bind_socket

    listen_socket

    write_listen_message

    mov w0, w19           ; return server_socket fd
    b .setup_socket_exit

.setup_socket_error:
    mov w0, #-1           ; return error code

.setup_socket_exit:
    stack.frame.destroy x12
    ret

.equiv STACK_SIZE_SETUP_SOCKET, 0x30
