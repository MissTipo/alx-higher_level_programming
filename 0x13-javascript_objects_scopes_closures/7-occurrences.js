#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { counter += 1; }
  }
  return counter;
};
const nbOccurences = require('./7-occurrences').nbOccurences;
console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(['S', 12, 'c', 'S', 'School', 8], 'S'));
