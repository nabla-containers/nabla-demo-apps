var ip = require("ip");

var webrepl = require('webrepl');
console.log('listening on http://' + ip.address() + ':8081/')
webrepl.start(8081);
