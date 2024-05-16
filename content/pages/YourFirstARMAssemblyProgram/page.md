# Your first ARM Assembly Program

This is a simple guide to writing your first ARM assembly program for linux. This guide will show you how to write a simple program that will print `Hello World` to the console.


## Installing required packages

You will need to install the following packages:

```bash
sudo apt-get update
sudo apt-get install build-essential
```

These packages are required to compile the program.

## Writing the program

Open a text editor like `vim` or `nano` and create a new file called `hello.s`:

```bash
nano hello.s
```

Or if you prefer `vim`:

```bash
vim hello.s
```

This should put you in a text editor. Copy the following into it:

```assembly
.section .data
    msg:
        .ascii "Hello world\n"
        len = . - msg

.section .text
    .globl _start

_start:
    mov x0, 1
    ldr x1, =msg
    ldr x2, =len
    mov x8, 64
    svc 0
    mov x8, 93
    mov x0, 0
    svc 0
```

Then save the file.

## Compiling the program

To compile our program we are going to use `as` ans `ld`. Run the following commands:

```bash
as -o hello.o hello.s
ld -o hello hello.o
```

This will create an executable called `hello`.

## Running the program

To run the program, simply run:

```bash
./hello
```

You should see `Hello world` printed to the console.

---
## See also

- [ARM - Wikipedia](https://en.wikipedia.org/wiki/ARM_architecture)
- [ARM documentation](https://developer.arm.com/documentation/dui0473/c/writing-arm-assembly-language)

## References

- [kerseykyle - ARM assembly hello world tutorial](http://kerseykyle.com/articles/ARM-assembly-hello-world)
- [Getting stated with ARM PDF](https://documentation-service.arm.com/static/64e7245d04d0d65e67136806)