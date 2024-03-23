#!/usr/bin/node
// Convert the first argument to an integer
const size = parseInt(process.argv[2]);

// Check if the conversion is successful and the result is not NaN
if (!isNaN(size)) {
  // Check if the size is greater than zero
  if (size > 0) {
    // Loop through rows
    for (let i = 0; i < size; i++) {
      // Create a string representing each row with 'X' characters
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      // Print the row
      console.log(row);
    }
  }
} else {
  // Print "Missing size" if size is not a valid number
  console.log('Missing size');
}
