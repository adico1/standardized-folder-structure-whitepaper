.section __TEXT,__text
.global multiply_numbers

multiply_numbers:
    mul x0, x0, x1                ; Multiply x0 and x1
    ret                           ; Return with the result in x0
