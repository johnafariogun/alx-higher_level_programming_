#!/usr/bin/node
const dict = require('./101-data.js').dict;
const new_ = {};
for (const key in dict) {
  if (new_[dict[key]]) {
    new_[dict[key]].push(key);
  } else {
    new_[dict[key]] = [key];
  }
}
console.log(new_);
