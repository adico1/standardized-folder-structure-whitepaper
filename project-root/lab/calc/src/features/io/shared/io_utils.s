.section __TEXT,__text
.global io_format

io_format:
    ; Dummy function to simulate formatting of IO data
    adr x1, io_str                 ; Load a simple IO string
    ret

io_str:
    .ascii "IO Operation: Done\n"
