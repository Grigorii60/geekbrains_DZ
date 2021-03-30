'use strict';
/*1
var a = 1, b = 1, c, d;
c = ++a; alert(c);           // 2 a=2 префиксной
d = b++; alert(d);           // 1 b=2 постфиксной
c = (2 + ++a); alert(c);      // 5 a=3 префиксной
d = (2 + b++); alert(d);      // 4 b=3 постфиксной
alert(a);                    // 3
alert(b);                    // 3
/*В постфиксной форме сначала происходит возвращение значения,
 а потом выполняется инкрементирование.
 В префиксной форме инкрементирование производится сразу,
 а возврат — уже с обновленным значением.*/

/*2
var a = 2;
var x = 1 + (a *= 2);
console.log(x)
/* Равен 5, тк сначала в скобках а=2*2, потом +1, и задается x*/

/*3
let a = parseInt(prompt('Enter the first number : '));
let b = parseInt(prompt('Enter the second number: '));

if (a >= 0 && b >= 0) {
    alert('Их разность равна: ' + (a - b));
} else if (a < 0 && b < 0) {
    alert('Их произведение равно: ' + (a * b));
} else if ((a >= 0 && b < 0) || (a < 0 && b >= 0)) {
    alert('Их сумма равна: ' + (a + b));
}
*/

/*4
let a = prompt('Please enter a number between 0 and 15 : ');

switch (a) {
    case '0':
        alert(0);
        break;
    case '1':
        alert('0;1');
        break;
    case '2':
        alert('0;1;2');
        break;
    case '3':
        alert('0;1;2;3');
        break;
    case '4':
        alert('0;1;2;3;4');
        break;
    case '5':
        alert('0;1;2;3;4;5');
        break;
    case '6':
        alert('0;1;2;3;4;5;6');
        break;
    case '7':
        alert('0;1;2;3;4;5;6;7');
        break;
    case '8':
        alert('0;1;2;3;4;5;6;7;8');
        break;
    case '9':
        alert('0;1;2;3;4;5;6;7;8;9');
        break;
    case '10':
        alert('0;1;2;3;4;5;6;7;8;9;10');
        break;
    case '11':
        alert('0;1;2;3;4;5;6;7;8;9;10;11');
        break;
    case '12':
        alert('0;1;2;3;4;5;6;7;8;9;10;11;12');
        break;
    case '13':
        alert('0;1;2;3;4;5;6;7;8;9;10;11;12;13');
        break;
    case '14':
        alert('0;1;2;3;4;5;6;7;8;9;10;11;12;13;14');
        break;
    case '15':
        alert('0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15');
        break;
}
*/

/*5
let arg1 = parseInt(prompt('Enter the first number : '));
let arg2 = parseInt(prompt('Enter the second number : '));

function add(arg1, arg2) {
    return (arg1 + arg2);
}
function mult(arg1, arg2) {
    return (arg1 * arg2);
}
function div(arg1, arg2) {
    return (arg1 / arg2);
}
function sub(arg1, arg2) {
    return (arg1 - arg2);
}

alert('Сложение равно: ' + add(arg1, arg2));
alert('Умножение равно: ' + mult(arg1, arg2));
alert('Деление равно: ' + div(arg1, arg2));
alert('Вычитание равно: ' + sub(arg1, arg2));
*/

/*6
let arg1 = parseInt(prompt('Enter the first number : '));
let arg2 = parseInt(prompt('Enter the second number : '));
let operation = prompt('Enter the required operation +,-,*,/ : ');

function add(arg1, arg2) {
    return (arg1 + arg2);
}
function mult(arg1, arg2) {
    return (arg1 * arg2);
}
function div(arg1, arg2) {
    return (arg1 / arg2);
}
function sub(arg1, arg2) {
    return (arg1 - arg2);
}

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+':
            return add(arg1, arg2);
        case '*':
            return mult(arg1, arg2);
        case '/':
            return div(arg1, arg2);
        case '-':
            return sub(arg1, arg2);
    }
}

alert('Результат операции: ' + mathOperation(arg1, arg2, operation))
*/

/*7
alert( null > 0 );  // (1) false
alert( null == 0 ); // (2) false
alert( null >= 0 ); // (3) true

Причина в том, что нестрогое равенство и сравнения > < >= <= работают по-разному.
Сравнения преобразуют null в число, рассматривая его как 0.
Поэтому выражение (3) null >= 0 истинно, а null > 0 ложно.

С другой стороны, для нестрогого равенства == значений undefined и
null действует особое правило: эти значения ни к чему не приводятся,
они равны друг другу и не равны ничему другому. Поэтому (2) null == 0 ложно.

*/

