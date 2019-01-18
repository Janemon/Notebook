const url = require('url');
const http = require('http');
const https = require('https');

const server = http.createServer((req, res) => {
    const path = url.parse(req.url).path.slice(1);
    console.log(req.url) // why just "/topics"?
  /*==You must know only browser has cross domin this concept, ther server is not! So we can use server to as proxy==*/
    if(path === 'topics') {
	    https.get('https://cnodejs.org/api/v1/topics', (resp) => {
	      let data = "";
	      resp.on('data', chunk => {
		    data += chunk;
	    });
	    resp.on('end', () => {
		res.writeHead(200, {
		    'Content-Type': 'application/json; charset=utf-8'
		});
		res.end(data);
	    });
	})
    }
}).listen(3000, '127.0.0.1');

console.log('启动服务，监听 127.0.0.1:3000');
