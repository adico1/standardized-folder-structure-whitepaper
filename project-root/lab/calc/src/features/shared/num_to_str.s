.section __TEXT,__text
.global num_to_str

num_to_str:
    adr x1, result_str           ; Dummy string result (in a real app, format X0)
    ret

result_str:
    .ascii "Result: 15\n"
