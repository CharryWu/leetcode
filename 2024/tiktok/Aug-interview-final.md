## What's the most representative project on your resume?

## What's the console output of following JS code?
```js
var result = []
var a = 3
var foo = function(a) {
    var i = 0;
    var total = 0;
    for (;i<3;i++) {
        result[i] = function() {
            total += i * a;
            console.log(total)
        }
    }
}
foo(1);
result[0]();
result[1]();
result[2]();
```

## What's the console output of following JS code?
```js
const p = new Promise((resolve, reject) => {
    console.log(1);
    resolve();
    console.log(2);
});

p.then((res) => {
    console.log(3);
})

console.log(4);
```
