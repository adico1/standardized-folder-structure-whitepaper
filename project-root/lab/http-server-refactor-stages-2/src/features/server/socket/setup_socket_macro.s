.ifndef __SETUP_SOCKET_MACROS
__SETUP_SOCKET_MACROS:

/* Macro to create a socket */
.macro create_socket
    mov w0, AF_INET       ; domain = AF_INET
    mov w1, SOCK_STREAM   ; type = SOCK_STREAM
    mov w2, IPPROTO_IP    ; protocol = IPPROTO_IP
    sys.socket
    cmp w0, #0
    b.lt .setup_socket_error
    mov w19, w0           ; store server_socket fd in w19
.endm

/* Macro to bind the socket */
.macro bind_socket
    mov x3, #0x0200       ; sin_len = 0, sin_family = PF_INET
    movk x3, #0xD204, lsl #0x10  ; sin_port = 1234
    movk x3, #0x0000, lsl #0x20  ; sin_addr = INADDR_ANY
    movk x3, #0x0000, lsl #0x30
    stack.store x3, VAR_server_address
    mov w0, w19           ; sockfd = server_socket
    stack.loadadr x1, VAR_server_address  ; *sockaddr = server_address
    mov w2, ADDRESS_LEN_SIZE  ; socklen_t = sizeof(server_address) = 16 bytes
    sys.bind
    cmp w0, #0
    b.ne .setup_socket_error
.endm

/* Macro to listen on the socket */
.macro listen_socket
    mov w0, w19           ; sockfd = server_socket
    mov w1, #1            ; backlog = 1
    sys.listen
    cmp w0, #0
    b.ne .setup_socket_error
.endm

/* Macro to write the listening message */
.macro write_listen_message
    mov w0, STDOUT
    adrp x1, message_listen@PAGE
    add x1, x1, message_listen@PAGEOFF
    adrp x2, message_listen_len@PAGE
    ldr w2, [x2, message_listen_len@PAGEOFF]
    sys.write
.endm

.endif
