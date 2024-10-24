.section __TEXT,__text
.global write_output

write_output:
    ; Simulated write (just print the number given in x0)
    bl print_message               ; Call the shared print function
    ret
