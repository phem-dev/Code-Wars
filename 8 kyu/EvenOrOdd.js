/*Instructions: 

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
*/

//Solution 1: Function with if/else statement

function evenOrOdd(number) {
  if (number % 2) {
    return "Odd";
  } else {
    return "Even";
  }
}

//Solution 2: Funtion with Ternary operators

function evenOrOdd(number) {
  return number % 2 ? "Odd" : "Even";
}
