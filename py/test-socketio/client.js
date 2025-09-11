const io = require('socket.io-client');
extra_data = {'X-Myapp-Ua': 'yyy'}
const args = process.argv
port = 8080
if (args.length > 2) {
    port = args[2]
}
console.log('port = ', port)
const socket = io('http://localhost:' + port + '/fanout', {
    extraHeaders: extra_data,
    // TODO: not working. too bad.
    localAddress: '192.168.77.28'
})
socket.on('connect', () => {
    console.log('connect')
    socket.send('raw message from client')
    socket.emit('my_event', 'event from client')
    socket.send({'k1': 'v1', 'k2': 'v2'})
})
socket.connect()
socket.on('message', (data) => {
    console.log('message =>', data)
})
socket.on('my_event', (data) => {
    console.log('message =>', data)
})
