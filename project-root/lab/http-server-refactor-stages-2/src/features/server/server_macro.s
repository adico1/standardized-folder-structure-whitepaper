.ifndef __SERVER_MACROS

.align 4

__SERVER_MACROS:

.macro setup_socket
    bl _setup_socket
    cmp w0, #0
    b.lt .setup_socket_failed
    mov w19, w0   ; store server_socket fd in w19
.endm

.macro handle_connections
    mov w0, w19
    bl _handle_connections
.endm

.macro close_server_socket
    mov w0, w19   ; sockfd = server_socket
    sys.close
.endm

.macro exit_success
    mov w0, #0    ; return success
.endm

.macro handle_setup_socket_error
    bl _handle_setup_socket_error
.endm

.endif

