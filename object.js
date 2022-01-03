const fs = require('fs')

const readFiles = fs.readFileSync('myfile.txt').toString('utf8').split('\n')

readFiles.map(value => console.log(`${value} --- `))