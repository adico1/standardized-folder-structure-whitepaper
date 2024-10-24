.ifndef __MACROS

.align 4

__MACROS:

.equiv SWI_SYSCALL, 0x80

.equiv SYS_exit, 1
.equiv SYS_read, 3
.equiv SYS_write, 4
.equiv SYS_close, 6
.equiv SYS_accept, 30
.equiv SYS_socket, 97
.equiv SYS_bind, 104
.equiv SYS_listen, 106
.equiv SYS_sendto, 133

.equiv STACK_entry_size, 0x10

/* Syscalls */

.macro sys.call
  svc SWI_SYSCALL
.endm

.macro sys.exit
  mov w16, SYS_exit
  sys.call
.endm

.macro sys.socket
  mov w16, SYS_socket
  sys.call
.endm

.macro sys.close
  mov w16, SYS_close
  sys.call
.endm

.macro sys.write
  mov w16, SYS_write
  sys.call
.endm

.macro sys.bind
  mov w16, SYS_bind
  sys.call
.endm

.macro sys.listen
  mov w16, SYS_listen
  sys.call
.endm

.macro sys.accept
  mov w16, SYS_accept
  sys.call
.endm

.macro sys.read
  mov w16, SYS_read
  sys.call
.endm

.macro sys.sendto
  mov w16, SYS_sendto
  sys.call
.endm

/* Stack */

.macro stack.frame.create $size
  sub sp, sp, STACK_entry_size
  sub sp, sp, \$size
  stp fp, lr, [sp]
  mov fp, sp
.endm

.macro stack.frame.destroy $size
  ldp fp, lr, [sp]
  add sp, sp, STACK_entry_size
  add sp, sp, \$size
.endm

.macro stack.store $reg, $offset
  stp \$reg, xzr, [fp, \$offset]
.endm

.macro stack.loadadr $reg, $offset
  add \$reg, fp, \$offset
.endm

.endif