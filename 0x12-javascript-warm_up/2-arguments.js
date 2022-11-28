#!/usr/bin/node
// import { argv } from 'node:process';
const argc = process.argv.length;
if (argc < 3) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
