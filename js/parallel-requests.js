const Event = require('events')
const https = require('https')

const uri = 'https://example.com'
const queries = ['a=1', 'b=2', 'c=3', 'd=4', 'e=5', 'f=6']
const requestEvent = new Event()
// Will have this many requests pending at any time
const numParallelRequests = +process.argv[2] || 1

requestEvent.on('next', () => {
	if (queries.length > 0) {
		sendRequest(queries.shift())
	}
})

// Dispatch first requests async.
for (let i = 0; i < numParallelRequests; i++) {
	setImmediate(() => {
		requestEvent.emit('next')
	})
}

function sendRequest(query) {
	https.get(`${uri}?${query}`, (res) => {
		console.log(res.statusCode, query)
		let body = ''

		res.on('data', (chunk) => {
			console.log(query, 'data')
			body += chunk
		})

		res.on('end', () => {
			console.log(query, 'end')
		})

		requestEvent.emit('next')  // Send another request
	})
}
