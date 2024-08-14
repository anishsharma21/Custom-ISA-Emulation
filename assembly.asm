.data
num1:   .word 10
num2:   .word 20
result: .word 0

.text
.global main
main:
ldr r0, =num1      
ldr r1, [r0]       

ldr r0, =num2      

ldr r2, [r0]       
add r3, r1, r2     

ldr r0, =result    
str r3, [r0]       

mov r7, #1         
swi 0              