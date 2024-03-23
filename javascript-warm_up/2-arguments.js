#!/usr/bin/node
const numAr = process.argv.length - 2;
if (numAr === 0) {
  console.log('No argument');
} else if (numAr === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
