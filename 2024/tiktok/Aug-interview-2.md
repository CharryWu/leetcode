## Write usePrevious hook
```js
const [value, setValue] = useState('');
const previous = usePrevious(value);
```

Solution:
```js
function usePrevious(value) {
    const prev = useRef();
    useEffect(() => {
        prev.current = value;
    }, [value]);
    return prev
}
```

## Array
What's the output of following code?
```js
function Foo(x) {
    getName = function() { console.log(1); }
    return this;
}
Foo.getName = function() { console.log(2); }
Foo.prototype.getName = function() { console.log(3); }
var getName = function() { console.log(4); }
function getName() { console.log(5); }

Foo.getName();
getName();
Foo().getName();
getName();
new Foo().getName();
new Foo.getName()
new new Foo().getName();
```

## Implement `pipe`
```js
const add2 = (x) => x+2
const mul2 = (x) => x*2
pipe(x, [add2, mul2]) // (x+2) * 2
```
Solution: use reduce
```js
function pipe(x, arr) {
    return arr.reduce((prev, func) => func(prev), x);
}
```
Follow-up: What does `this` inside func when calling pipe refer to?
Ans: `this` inside func inherits its context from parent scope. The arrow function

## Subset
