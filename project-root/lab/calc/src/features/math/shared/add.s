.section __TEXT,__text
.global add_numbers

add_numbers:
    add x0, x0, x1              ; Add x0 and x1, result in x0
    ret                         ; Return to caller
