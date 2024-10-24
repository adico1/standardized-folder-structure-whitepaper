.equiv AF_INET, 0x2
.equiv SOCK_STREAM, 0x1
.equiv IPPROTO_IP, 0x0

.equiv STDOUT, 1

.equiv REQUEST_BUFFER_SIZE, 4096
.equiv ADDRESS_SIZE, 0x10
.equiv ADDRESS_LEN_SIZE, 0x10

.equiv STACK_SIZE_HANDLE_CONNECTIONS, REQUEST_BUFFER_SIZE + ADDRESS_SIZE + ADDRESS_LEN_SIZE

.equiv VAR_server_address, 0x10
.equiv VAR_client_address, 0x20
.equiv VAR_client_address_len, 0x30
.equiv VAR_request_buffer, 0x40
