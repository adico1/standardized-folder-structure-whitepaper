.include "./src/shared/macros.s"
.include "./src/features/server/shared/constants.s"
.include "./src/features/server/connection_handler/connection_handler_macro.s"
.include "./src/features/server/connection_handler/messages.s"

.global _handle_connections

.text
.align 4

_handle_connections:
    mov x12, STACK_SIZE_HANDLE_CONNECTIONS
    stack.frame.create x12

    mov w19, w0  ; store server_socket fd in w19

    loop:
        // Accept connection
        accept_connection w10, error_accept

        // Handle client request
        handle_client_request w10, error_read

        // Write request to STDOUT
        write_request_to_stdout

        // Send response
        send_response w10, error_send

        // Close client socket
        close_client_socket w10

        b loop

    mov w0, #0
    b handle_connections_exit

error_accept:
    print_error_message error_message_accept, error_message_accept_len
    b handle_connections_exit

error_read:
    print_error_message error_message_read, error_message_read_len
    b handle_connections_exit

error_send:
    print_error_message error_message_send, error_message_send_len

handle_connections_exit:
    stack.frame.destroy x12
    ret
