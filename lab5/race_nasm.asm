section .data
    global shared_counter
    shared_counter dq 0

section .text
    global thread_function

thread_function:
    mov rcx, 10000000

.loop:
    mov rax, [rel shared_counter]
    inc rax
    mov [rel shared_counter], rax
    loop .loop

    xor rax, rax
    ret
