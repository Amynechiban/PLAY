function Send(){

let message = document.getElementById('message').value;
let name = document.getElementById('Name').value;

let data = '\r ' + name.value + '\r: '+ message.value +'\n';
const fs = require('fs');

fs.writeFile('Output.txt', data, (err) => {
      
    // In case of a error throw err.
    if (err) throw err;
})


}