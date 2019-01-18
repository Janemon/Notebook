const Url=require("url")
const Http=require("http")
Http.createServer((req, res)=>{
  const data={
    x: 10
  }
  /*==get the callback_function, in request'url==*/
  const callback=Url.parse(req.url, true).query.callback
  console.log(req.url) // I know that, the path is exclude the domain's name!! so we can see "/....."
  res.writeHead(200)
  /*==return the data with callback_function filled with server's data, the callback_function is request's url set ==*/
  res.end(`${callback}(${JSON.stringify(data)})`)
}).listen(3000, "127.0.0.222")
console.log(`Server builded, listen "127.0.0.222:3000"`)
