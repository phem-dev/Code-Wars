/*Instructions:
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.

*/

//Solution:

function positiveSum(arr) {
  let sum = 0; // Initialized a variable called "sum" to 0

  //For loop to loop through array elements
  for (let i = 0; i < arr.length; i++) {
    //If element is > 0, add its value to sum
    if (arr[i] > 0) sum += arr[i];
  }
  return sum;
}

positiveSum([1, 2, 3, 4, 5]);
