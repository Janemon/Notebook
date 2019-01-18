const Http=require("http")
Http.createServer((req,res)=>{
  res.writeHead(200,{
    "Access-Control-Allow-Origin": "http://127.0.0.1:8080"
  })
  res.end("this is the data you want: '111' ")
}).listen(3000, "127.0.0.1")
console.log("server builded, listen '127.0.0.1:3000'")
