{
    let a=10;
    var b=1;
}


var a=[]
for(let i=0;i<10;i++){
    console.log(i)
    a[i]=function(){
        console.log(i)
    }
}


// ES5 环境
function f() { console.log('I am outside!'); }

(function () {
  function f() { console.log('I am inside!'); }
  if (false) {
  }
  f();
}());

