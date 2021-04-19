'use strict';

/*1. Создать функцию, генерирующую шахматную доску.
При этом можно использовать любые html-теги по своему желанию.
Доска должна быть разлинована соответствующим образом, т.е. чередовать
черные и белые ячейки. Строки должны нумероваться числами от 1 до 8,
столбцы – латинскими буквами A, B, C, D, E, F, G, H.
*/
/*
let fistLine = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];

function chessBoard(fistLine) {
    var table = document.createElement("table");

    for (var row = 0; row < 9; row++) {
        var tr = document.createElement('tr');

        for (var col = 0; col < 9; col++) {
            var td = document.createElement('td');

            if (col % 2 == row % 2 && col > 0 && row !== 0) {
                td.className = "white";
            } else if (col % 2 !== row % 2 && col > 0 && row !== 0) {
                td.className = "black";
            } else if (row == 0 && col > 0) {
                td.className = "white";
                td.innerHTML = fistLine[col];
            } else if (row > 0 && col == 0) {
                td.className = "white";
                td.innerHTML = row;
            } else {
                td.className = "white";
            }

            tr.appendChild(td);
            tr.className = "tr";
        }
        table.appendChild(tr);
    }
    document.body.appendChild(table);
}

chessBoard(fistLine);
*/

/*2

const basket = {
    arr: [
        {
            blockName: 'смартфон',
            price: 10000,
            name: 'Нокиа',
            quantity: 0
        },
        {
            blockName: 'телефон',
            price: 2000,
            name: 'Нокиа',
            quantity: 0
        },
        {
            blockName: 'планшет',
            price: 8000,
            name: 'Нокиа',
            quantity: 0
        },
        {
            blockName: 'чехол',
            price: 10000,
            name: 'Нокиа',
            quantity: 0
        }
    ],

    countBasketPrice() {
        let allPrice = this.arr.reduce((totalPrice, cartItem) => totalPrice + cartItem.price * cartItem.quantity, 0);
        let allQuantity = this.arr.reduce((totalQuantity, cartItem) => totalQuantity + cartItem.quantity, 0);
        if (allPrice == 0) {
            return 'Корзина пуста.';
        } else {
            return 'В корзине ' + allQuantity + ' товаров на сумму ' + allPrice + ' рублей.';
        }
    },
};

//alert(basket.countBasketPrice());

let basketD = document.createElement("basket");
basketD.innerHTML = basket.countBasketPrice();
document.body.appendChild(basketD);
*/