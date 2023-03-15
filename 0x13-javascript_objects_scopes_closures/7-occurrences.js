#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, alph) => alph === searchElement ? count + 1 : count, 0);
};
