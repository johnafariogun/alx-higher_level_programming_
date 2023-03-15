#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, cha) { array.push(cha); return array; }, []);
};
