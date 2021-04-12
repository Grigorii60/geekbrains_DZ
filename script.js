'use strict';

/*1

let sepNumber = {};

let number = parseInt(prompt('Please enter a number between 0 and 999: '));

function separat(number) {

    if (number > 999) {
        console.log('Число превышает 999.');
        alert('Число превышает 999.')
        return sepNumber;
    } else {
        let units = number % 10;
        sepNumber.единицы = units;
        number = (number - units) / 10
        console.log(number);
        let tens = number % 10;
        sepNumber.десятки = tens;
        let hundreds = (number - tens) / 10
        sepNumber.сотни = hundreds;
        return sepNumber;
    };
};

console.log(separat(number));

*/

/*2
const basket = {
    arr: [
        ['смартфон', 10000, 'Нокиа', 1],
        ['телефон', 2000, 'Нокиа', 0],
        ['планшет', 8000, 'Нокиа', 2],
        ['чехол', 10000, 'Нокиа', 1],
    ],
    init(arr) {
        this.arr = arr;
    },

    countBasketPrice() {
        let add = 0;
        for (let i = 0; i < this.arr.length; i++) {
            add += (this.arr[i][1] * this.arr[i][3]);
        };
        return add
    },
};

alert(basket.countBasketPrice());

*/