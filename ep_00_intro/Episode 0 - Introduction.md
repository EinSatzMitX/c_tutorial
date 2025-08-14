This is the introduction to the C Programming Language Tutorial. In this episode you will learn:
-  What is C?
-  What versions of C are there?
-  Why should I learn C in 2025?
-  What programs are required for the tutorial?
- How do I write and compile my first C program?
<div align="center" style="display: flex; justify-content: space-evenly;">
  <img src="Pasted image 20250306134158.png" width="500" alt="Ken Thompson and Dennis Ritchie" />
  </div>
_Picture of Ken Thompson (left) and Dennis Ritchie (right)_

## What is C?

---
C is a Compiled Programming Language, developed by Dennis Ritchie, the creator of Unix, and it first appeared in 1972
The C Programming Language is often used in Low Level environments, such as Operating Systems or Embedded Systems because it can be compiled to Bare Metal and doesn't require any additional software. 
C is useful because it has basically no runtime requirements and it is extremely fast.
C is also useful because when reading code written in C, you can directly tell what the machine is doing in every single line of code, however the language still abstracts enough logic to be a lot easier to understand and use than assembly.
There are a lot of Compilers for C but the most common ones are GCC (GNU Compiler Collection) and Clang (LLVM-based compiler).
I this tutorial, I will be using clang, however you will probably be able to follow along just fine if you decide to use gcc for the first few episodes.

## What versions of C are there?

---
C is a very old language and over time many versions of the language have emerged. To make this cleaner and better reproducible, Programmers have agreed on versions of the C.
Here is a list of all official C standards

| Year                                         | Informal name           | Official standard                   |
| -------------------------------------------- | ----------------------- | ----------------------------------- |
| 1972                                         | first release           | -                                   |
| 1978                                         | K&R C                   | -                                   |
| 1989, 1990                                   | ANSI C, C89, ISO C, C90 | ANSI X3.159-1989  ISO/IEC 9899:1990 |
| 1999                                         | C99, C9X, "modern C"    | ISO/IEC 9899:1999                   |
| 2011                                         | C11, C1X                | ISO/IEC 9899:2011                   |
| 2018                                         | C17, C18                | ISO/IEC 9899:2018                   |
| 2024                                         | C23, C2X, "latest C"    | ISO/IEC 9899:2024                   |
| <abbr title="To be announced">TBA</abbr><br> | C2Y                     | ...                                 |
In this Tutorial series, I will probably be referring to C99 as "modern C", because it is the most used version of C and it has most modern features you want.

## Why should i learn C in 2025?

---
You might ask yourself, "Why should i learn a language, that is over half a century old?!"
And that is a reasonable question. However C is still one of the most used languages in modern applications, even after all this time. C is the heart of all modern infrastructure and it's safe to say, that without it, the world wouldn't be the same. Most modern programming languages also have bindings for C, meaning that you can use and interact with code written in C directly in the other language.
C is preferred in low-level environments, like in Embedded Software or Operating Systems because it abstracts the Machine code enough to make it easier to use, but not too much, so that you can still tell what the machine is doing in every line of code. 
This makes it so suited for very time critical applications.

## What programs are required for the tutorial?

---
Now, that you hopefully are interested in learning C, what software is required for following the tutorial?
- A code editor, I like to to use Neovim, however for beginners I would recommend using VSCode, as it is dead simple to set up and provides you with features like Syntax highlighting and access to a shell out of the box
	- If you decided to use VSCode, I also recommend installing the C/C++ Extensions Pack
- Speaking of which, you need access to a Unix-like shell (e.g. bash on Ubuntu Linux) (Don't worry, if you don't know what a shell is, using it is very simple and when following the tutorial, you won't get stuck anywhere)
	- If you are using Windows, i strongly encourage you to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem or Linux) 
	- If you are on MacOS X, you should be able to access a terminal and install all necessary programs, however I have no idea how, I luckily never had to use a Mac)
	- If you are on Linux, or anything else, you probably already know, what a Terminal and a shell are and how you get programs installed
- A C Compiler (GCC 14.0 or higher / Clang 19.0 or higher)(As I already mentioned, I will be using Clang)
	- If you are on WSL or Ubuntu, run `sudo apt update`, followed by `sudo apt install build-essential` (for gcc) or `sudo apt install clang`

## How do I write and compile my first C program?

---
To make sure that you got everything working correctly, let's write our first tiny program:
```C
// Call this file main.c

// This line makes the "printf" function available to us
#include <stdio.h>

// The entry point of our program
int main(int argc, char** argv /* Don't worry about these two for now */){
	// Print out something to the command line
	printf("Hello, World!\n");

	// Exit our program with the exit code 0, which stands for success
	return 0;
}
```
and compile it with one of these two commands
```
gcc main.c -o main

clang main.c -o main
```
you should be able to run it now
```
❯ ./main
Hello, World!
```

And voilà! That is you first program written in C! :D