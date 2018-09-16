function foo(c,b){
  var a;
  if((typeof c) == "number" && (typeof b) =="number"){
    a=c+b;
    return a;
  }
  console.log("NaN");
  return NaN;
}
foo(1,2);

