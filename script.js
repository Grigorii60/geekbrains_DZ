'use strict';

/*1

let i = 2;

newPr: while (i < 100) {
    let j = 2;
    while (j < i) {
        if (i % j == 0) {
            i++;
            continue newPr;
        } else {
            j++;
        }
    }
    alert(i);
    i++;

}
*/

/*2
let arr = [
    ['смартфон', 10000, 'Нокиа', 1],
    ['телефон', 2000, 'Нокиа', 0],
    ['планшет', 8000, 'Нокиа', 1],
    ['чехол', 10000, 'Нокиа', 1],
];

function countBasketPrice(arr) {
    let add = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i][3] == 1) {
            add += arr[i][1];
        }
    }
    return add
};

alert(countBasketPrice(arr));
*/

/*3
for (let i = 0; i < 9; alert(i), i++) { }
*/

/*4
let text = 'x';
console.log(text);
for (let i = 0; i < 20; i++) {
    console.log(text += 'x');
};
*/