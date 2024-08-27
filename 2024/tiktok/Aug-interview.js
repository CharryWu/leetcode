// What's the output of the following code?
const p = new Promise((resolve, reject) => {
    console.log(1);
    resolve();
    console.log(2);
})

p.then(() => {
    console.log(3);
})

console.log(4);

// 1 2 4 3

// Implement a function that flattens a nested array with level as a parameter
function flatten(arr, level) {
    let res = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            if (level > 1) {
                res = res.concat(flatten(arr[i], level - 1));
            } else {
                res = res.concat(arr[i]);
            }
        } else {
            res.push(arr[i]);
        }
    }
    return res;
}

// How to implement custom js array methods that add a value to each element?
[1,2,3,4,5].func(1) // [2,3,4,5,6]
Array.prototype.func = function(a1) {
    for (let i = 0; i < this.length; i++) {
        this[i] += a1;
    }
    return this;
}

// implement useDebounce hook
function useDebounce(value, delay) {
    const [debouncedValue, setDebouncedValue] = useState(value);
    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);
        return () => {
            clearTimeout(handler);
        };
    }, [value, delay]);
    return debouncedValue;
}
