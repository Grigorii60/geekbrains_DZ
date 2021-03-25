'use strict';
let Tc = prompt('Enter grauses in Celsius: ');
let Tf = (9 / 5) * Tc + 32;
alert('Degrees in Fahrenheit: ' + Tf);

let admin;
let name;
name = 'Василий';
admin = name;
alert(admin);

alert(1000 + '108');

/*
Если не важно загрузилась ли страница, то используем async.
Если нужно, что бы скрипт запускался после страницы, то defer
*/