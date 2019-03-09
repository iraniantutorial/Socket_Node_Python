const io = require("socket.io-client");
const socket = io.connect("http://localhost:5555");

socket.on('welcome', function(data) {
	console.info(data.message);

	socket.emit('i am client', {data: 'foo!', id: data.id});
});

socket.on("time", (msg) => console.info(msg));

