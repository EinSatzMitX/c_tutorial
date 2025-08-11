
---
In this episode you will learn:
- [x] What is a variable?
- [x] Basic variable types
- [ ] How to print out variables using format specifiers

## What is a variable?

---
This episode might be a bit boring if you already know another programming language, however it is essential to understand if you want to learn C, or almost any programming language.
In programming languages, you often handle data. This data can be an integer, a decimal,  but it can also be a character, or a string of characters. It can be a list, a Hashmap, etc.
All these different data types can be stored in something called a "variable". You can think of your computers Memory as a giant desk cabinet with many, many drawers. These drawers are the small space that hold our data, so they're the variables. 
In computers, data is represented using 1s and 0s, and it is the programming languages, but also the programmers task to correctly interpret this data.
For example, the character `'A'` is represented with `0b01000001` (0b is just a prefix to indicate a binary number) or the number `65` in the decimal system.
This allows us to do some cool tricks in C, for example we can add `'A' + 5` and get `'F'` as a result.

## Basic variable types

---
Here are the most used simple data types in C
```C
/* Added in C23 */
bool b; /* 1 Byte of storage, can hold values from 0 to 255, but it's only used for false(0) and true(1, but any other value also counts as true)*/
// As you see, variables dont just have types and values, they also have a name to make it lifes easier for programmers. This boolean variable is simply called "b"

/* Character types */
char c; /* 1 Byte of storage, used for holding character or "string" values */
unsigned char uc; /* 1 Byte of storage, also used for storing characters or strings*/

/* Integer number types */
short s; /* 2 Bytes of storage, can hold integer number from -2^15 to 2^15 - 1 */
int i; /* 4 Bytes of storage, can hold integer numbers from -2^31 to 2^31-1 */

long l; /* 8 Bytes of storage, can hold integer values from -2^63 to 2^63 -1 */

// NOTE: All integer number types can be prefixed with either 'signed' or 'unsigned' to make them range from negative to postive or only positive respectively


/* Floating point number types */
float f; /* 4 Bytes of storage, can hold decimal values from ±1.18×10−38 to ±3.4×1038 (ca. 7 decimal digits precision */

double d; /* 8 Bytes of storage, can hold decimal values from ±2.23×10−308 to ±1.80×10308 (ca. 16 decimal digits precision */
```

As some may have noticed, there are no Strings in C by default, however this does not mean you can't handle blocks of text. String are represented with something called Pointers, but more about that later.

## How to print out variables using format specifiers

---
Now that you know most of the primitive data types, let's write some code:
```C
// main.c
include <stdio.h>

int main(int argc, char **argv) {
  int a = 0;
  int b = 5;
  /* Print both integers as integers to the command line */
  printf("a: %i, b: %i\n", a, b);

  char c = 'A';
  /* Print out c as a character */
  printf("c: %c\n", c);

  /* We can actually do some cool tricks in C */
  /* We can add c and b together and then print the result as a character */
  /* To do this however, we have to _cast_ b to a char */
  printf("c+a: %c\n", c + (char)b);

  /* To tell the compiler, that a number is a float, we can suffix it with an
   * 'f' */
  float d = 5.99f;
  /* Print out d as a floating point number */
  printf("d: %f\n", d);

  /* Again, we can add the two numbers together, however we have to cast b to a
   * float first */
  printf("d+b: %f\n", d + (float)b);

  return 0;
}

```