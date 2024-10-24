.include "./src/shared/macros.s"
.include "./src/features/server/shared/constants.s"
.include "./src/features/server/server_macro.s"

.global _server_main
.extern _setup_socket
.extern _handle_connections
.extern _handle_setup_socket_error

.text
.align 4

.equiv STACK_SIZE_SERVER_MAIN, 0x20  // Adjust this size as needed

/* Our main function where we set up the socket and start handling connections */
_server_main:
    mov x12, STACK_SIZE_SERVER_MAIN
    stack.frame.create x12

    setup_socket

    handle_connections

    close_server_socket

    exit_success
    b .server_main_exit

.setup_socket_failed:
    handle_setup_socket_error

.server_main_exit:
    stack.frame.destroy x12
    ret
