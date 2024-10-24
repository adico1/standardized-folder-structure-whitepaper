.global main
.align 4
.text

.include "./src/macros.s"

.equiv AF_INET, 0x2
.equiv SOCK_STREAM, 0x1
.equiv IPPROTO_IP, 0x0

.equiv STDOUT, 1

.equiv REQUEST_BUFFER_SIZE, 4096
.equiv ADDRESS_SIZE, 0x10
.equiv ADDRESS_LEN_SIZE, 0x10

.equiv STACK_SIZE_MAIN, REQUEST_BUFFER_SIZE + ADDRESS_SIZE + ADDRESS_LEN_SIZE

.equiv VAR_server_address, 0x10
.equiv VAR_client_address, 0x20
.equiv VAR_client_address_len, 0x30
.equiv VAR_request_buffer, 0x40

/* Error messages */
error_message_socket: .string "Could not create socket\n"
error_message_socket_len = . - error_message_socket
.align 2
error_message_bind: .string "Could not bind to port\n"
error_message_bind_len = . - error_message_bind
.align 2
error_message_listen: .string "Error while listening\n"
error_message_listen_len = . - error_message_listen
.align 2
error_message_accept: .string "Error while accepting\n"
error_message_accept_len = . - error_message_accept
.align 2
error_message_read: .string "Error while reading\n"
error_message_read_len = . - error_message_read
.align 2
error_message_send: .string "Error while sending data\n"
error_message_send_len = . - error_message_send
.align 2

/* Messages */
message_listen: .string "Listening for connections\n\n"
message_listen_len = . - message_listen
.align 2
response: .string "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 15\r\n\r\nHello, world!\n"
response_len = . - response
.align 2

main:
  mov x12, STACK_SIZE_MAIN
  stack.frame.create x12

  mov w0, AF_INET                                       ; domain = AF_INET
  mov w1, SOCK_STREAM                                   ; type = SOCK_STREAM
  mov w2, IPPROTO_IP                                    ; protocol = IPPROTO_IP
  sys.socket

  b.cs error_socket                                     ; if carry flag is set, jump to error_socket

  mov w19, w0                                           ; store server_socket fd in x19

  mov  x3, #0x0200                                      ; sin_len = 0, sin_family = PF_INET
  movk x3, #0xD204, lsl #0x10                           ; sin_port = 1234
  movk x3, 0x0000, lsl #0x20                            ; sin_addr = INADDR_ANY
  movk x3, 0x0000, lsl #0x30                            ; ...

  stack.store x3, VAR_server_address                    ; store server_address to the stack

  mov w0, w19                                           ; sockfd = server_socket;
  stack.loadadr x1, VAR_server_address                  ; *sockaddr = server_address;
  mov w2, ADDRESS_LEN_SIZE                              ; socklen_t = sizeof(server_address) = 16 bytes
  sys.bind

  cmp x0, xzr
  b.ne error_bind

  mov w0, w19                                           ; sockfd = server_socket;
  mov w1, #1                                            ; backlog = 1
  sys.listen

  b.cs error_listen

  mov w0, STDOUT
  adr x1, message_listen
  ldr x2, =message_listen_len
  sys.write

  /* Our main loop where we listen and respond to incoming connections */
  loop:
    stack.loadadr x7, VAR_client_address                ; load *client_address

    mov w0, w19                                         ; sockfd = server_socket;
    mov x1, x7                                          ; *address = client_address;
    stack.loadadr x2, VAR_client_address_len            ; *address_len;
    sys.accept

    b.cs error_accept

    mov w10, w0                                         ; store client_socket fd in w10

    mov w0, w10
    stack.loadadr x1, VAR_request_buffer                ; *buffer = buffer;
    mov x2, REQUEST_BUFFER_SIZE                         ; length = REQUEST_BUFFER_SIZE;
    sys.read

    b.cs error_read

    stack.loadadr x1, VAR_request_buffer
    mov x2, x0
    mov x0, STDOUT
    sys.write

    mov w0, w10                                         ; sockfd = client_socket;
    adr x1, response                                    ; *buffer = response;
    ldr x2, =response_len                               ; length = response_len;
    mov w3, #0                                          ; flags = 0;
    mov w4, wzr                                         ; *dest_addr = 0;
    mov w5, wzr                                         ; dest_len = 0;
    sys.sendto

    b.cs error_send

    b loop

  mov w0, w19                                           ; sockfd = server_socket;
  sys.close

  stack.frame.destroy x12

  mov w0, wzr
  sys.exit

  error_socket:
    mov w19, w0
    mov w0, STDOUT
    adr x1, error_message_socket
    ldr x2, =error_message_socket_len
    sys.write

    mov w0, w19
    sys.exit

  error_bind:
    mov w19, w0
    mov w0, STDOUT
    adr x1, error_message_bind
    ldr x2, =error_message_bind_len
    sys.write

    mov w0, w19
    sys.exit

  error_listen:
    mov w19, w0
    mov w0, STDOUT
    adr x1, error_message_listen
    ldr x2, =error_message_listen_len
    sys.write

    mov w0, w19
    sys.exit

  error_accept:
    mov w19, w0
    mov w0, STDOUT
    adr x1, error_message_accept
    ldr x2, =error_message_accept_len
    sys.write

    mov w0, w19
    sys.exit

  error_read:
    mov w19, w0
    mov w0, STDOUT
    adr x1, error_message_read
    ldr x2, =error_message_read_len
    sys.write

    mov w0, w19
    sys.exit

  error_send:
    mov w19, w0
    mov w0, STDOUT
    adr x1, error_message_send
    ldr x2, =error_message_send_len
    sys.write

    mov w0, w19
    sys.exit