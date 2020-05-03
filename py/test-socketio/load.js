const io = require('socket.io-client');
const args = process.argv
port = 8080
if (args.length > 2) {
    port = args[2]
}
bind_address = '192.168.1.186'
console.log('connect port =>', port)
namespace = '/fanout'
function create_connection(port) {
    const socket = io('http://127.0.0.1:' + port + namespace, {
        // TODO: not working. too bad.
        localAddress: bind_address,
        extraHeaders: {
            room: 10
        }
    })
    socket.on('connect', () => {
        console.log('connect')
    })
    socket.on('connect_error', (res) => {
        console.log('connect error =>', res)
    })
    socket.connect()
    socket.on('message', (data) => {
        console.log('message =>', data)
    })
    socket.on('my event', (data) => {
        console.log('message =>', data)
    })
    return socket
}

socket = create_connection(port)

