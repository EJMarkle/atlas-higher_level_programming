#!/usr/bin/node
// Define the add function with prototype function add(a, b)
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

// Get the command-line arguments and call the add function with them
const result = add(process.argv[2], process.argv[3]);

// Print the result
console.log(result);
