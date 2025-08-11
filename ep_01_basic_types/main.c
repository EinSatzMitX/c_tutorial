#include <stdio.h>

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
