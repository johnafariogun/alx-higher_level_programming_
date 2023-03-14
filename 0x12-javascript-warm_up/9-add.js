#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
const y = Math.floor(Number(process.argv[3]));
if (x && y) {
    console.log(x + y);
} else {
  console.log('NaN');
}
