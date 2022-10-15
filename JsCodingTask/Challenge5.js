// task_5

//    Create a function that reverses an array



let a = [10, 8, 6, 4, 2];
let b = reverseArray(a);
console.log(b);

function reverseArray(a)
{
    let b = [];
    
    for(let i = a.length - 1; i >= 0; i--)
    {
        b.push(a[i]);
    }
    
    return b;
}
    



