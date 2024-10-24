.data
/* Error messages for connection handling */
error_message_accept: .string "Error while accepting connection\n"
error_message_read: .string "Error while reading request\n"
error_message_send: .string "Error while sending response\n"

response: .string "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 15\r\n\r\nHello, world!\n"


.align 4
error_message_accept_len: .word . - error_message_accept
error_message_read_len: .word . - error_message_read
error_message_send_len: .word . - error_message_send

response_len: .word . - response
