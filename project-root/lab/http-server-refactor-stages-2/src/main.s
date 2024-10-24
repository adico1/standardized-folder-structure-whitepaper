.include "./src/shared/macros.s"

.extern _server_main

.global _main

.text
.align 4

_main:
    b _server_main
