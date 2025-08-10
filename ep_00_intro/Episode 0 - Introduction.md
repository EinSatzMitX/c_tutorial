This is the introduction to the C Programming Language Tutorial. In this episode you will learn:
-  What is C?
-  Why should I learn C in 2025?
-  What programs are required or the tutorial?

C is a Compiled Programming Language, developed by Dennis Ritchie, the creator of Unix, and it first appeared in 1972

![[Pasted image 20250306134158.png]]
_Picture of Ken Thompson (left) and Dennis Ritchie (right)_

The C Programming Language is often used in Low Level environments, such as Operating Systems or Embedded Systems because it can be compiled to Bare Metal and doesn't require any additional software. 
There are a lot of Compilers for C but the most common ones are GCC (GNU Compiler Collection) and Clang (LLVM-based compiler).

I this tutorial, I will be using clang, however you will probably be able to follow along just fine if you decide to use gcc for the first few episodes.

You might ask yourself, "Why should i learn a language, that is over half a century old?!"
And that is a reasonable question. However C is still one of the most used languages in modern applications, even after all this time. C is the heart of all modern infrastructure and it's safe to say, that without it, the world wouldn't be the same. Most modern programming languages also have bindings for C, meaning that you can use and interact with code written in C directly in the other language.
C is preferred in low-level environments, like in Embedded Software or Operating Systems because it abstracts the Machine code enough to make it easier to use, but not too much, so that you can still tell what the machine is doing in every line of code. 
This makes it so suited for very time critical applications.

Now, that you hopefully are interested in learning C, what software is required for following the tutorial?
- A code editor, I like to to use Neovim, however for beginners I would recommend using VSCode, as it is dead simple to set up and provides you with features like Syntax highlighting and access to a shell out of the box
	- If you decided to use VSCode, I also recommend installing the C/C++ Extensions Pack
- Speaking of which, you need access to a Unix-like shell (e.g. bash on Ubuntu Linux) (Don't worry, if you don't know what a shell is, using it is very simple and when following the tutorial, you won't get stuck anywhere)
	- If you are using Windows, i strongly encourage you to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem or Linux) 
	- If you are on MacOS X, you should be able to access a terminal and install all necessary programs, however I have no idea how, I luckily never had to use a Mac)
	- If you are on Linux, or anything else, you probably already know, what a Terminal and a shell are and how you get programs installed
- A C Compiler (GCC 14.0 or higher / Clang 19.0 or higher)(As I already mentioned, I will be using Clang)
	- If you are on WSL or Ubuntu, run `sudo apt update`, followed by `sudo apt install build-essential` (for gcc) or `sudo apt install clang`

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