'use strict';

/*1. Создать функцию, генерирующую шахматную доску.
При этом можно использовать любые html-теги по своему желанию.
Доска должна быть разлинована соответствующим образом, т.е. чередовать
черные и белые ячейки. Строки должны нумероваться числами от 1 до 8,
столбцы – латинскими буквами A, B, C, D, E, F, G, H.
*/
//let a = ['', A, B, C, D, E, F, G, H];

var table = document.createElement("table");

for (var row = 0; row < 9; row++) {
    var tr = document.createElement('tr');
    if (row = 0) {
        for (var col = 0; col < 9; col++) {
            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerHTML = 5;
        }
    } else {
        for (var col = 0; col < 9; col++) {
            var td = document.createElement('td');

            if (col % 2 == row % 2 && col > 0) {
                td.className = "white";
            } else if (col % 2 !== row % 2 && col > 0) {
                td.className = "black";
            } else {
                td.innerHTML = row;
            }
            tr.appendChild(td);
        }
    }
    table.appendChild(tr);
}

document.body.appendChild(table);

