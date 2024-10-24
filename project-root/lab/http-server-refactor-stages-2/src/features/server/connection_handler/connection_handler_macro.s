.ifndef __CONNECTION_HANDLER_MACROS
__CONNECTION_HANDLER_MACROS:

/* Common Logic Macros */

/* Load address into a register */
.macro load_address reg, offset
    stack.loadadr \reg, \offset
.endm

/* Check for error and branch */
.macro check_error_and_branch reg, error_label
    cmp \reg, #0
    b.lt \error_label
.endm

/* Setup system call */
.macro setup_syscall syscall_number
    mov w16, \syscall_number
    sys.call
.endm

/* Load response address and length */
.macro load_response
    adrp x1, response@PAGE
    add x1, x1, response@PAGEOFF
    adrp x2, response_len@PAGE
    ldr w2, [x2, response_len@PAGEOFF]
.endm

/* Connection Handling Macros */

/* Accept a connection and handle errors */
.macro accept_connection client_socket, error_label
    load_address x1, VAR_client_address
    mov w0, w19  // server_socket is stored in w19
    load_address x2, VAR_client_address_len
    setup_syscall SYS_accept
    mov \client_socket, w0
    check_error_and_branch \client_socket, \error_label
.endm

/* Close the client socket */
.macro close_client_socket client_socket
    mov w0, \client_socket
    setup_syscall SYS_close
.endm

/* Request Handling Macros */

/* Handle client request and handle errors */
.macro handle_client_request client_socket, error_label
    mov w0, \client_socket
    load_address x1, VAR_request_buffer
    mov w2, REQUEST_BUFFER_SIZE
    setup_syscall SYS_read
    check_error_and_branch w0, \error_label
.endm

/* Write client request to STDOUT */
.macro write_request_to_stdout
    load_address x1, VAR_request_buffer
    mov x2, x0
    mov w0, STDOUT
    setup_syscall SYS_write
.endm

/* Response Handling Macros */

/* Send response and handle errors */
.macro send_response client_socket, error_label
    mov w0, \client_socket
    load_response
    mov w3, #0
    mov w4, wzr
    mov w5, wzr
    setup_syscall SYS_sendto
    check_error_and_branch w0, \error_label
.endm

/* Error Handling Macros */

/* Print error message */
.macro print_error_message message, message_len
    mov w0, STDOUT
    adrp x1, \message@PAGE
    add x1, x1, \message@PAGEOFF
    adrp x2, \message_len@PAGE
    ldr w2, [x2, \message_len@PAGEOFF]
    setup_syscall SYS_write
.endm

.endif
