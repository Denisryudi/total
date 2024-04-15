const lista = [1, 2, 3, 4, 5];
console.log(lista[0]);

console.log(`O valor do elemento 3 da minha lista é ${lista[4]}`);



//### 2 - Escreva um programa executandos os próximos passos:    
//
  //  -Crie uma variável com valor inicial de um objeto que represente um pokemon (nome, estamina, defesa, ataque, habilidade).
//
  //  -Imprima na tela os textos "Meu objeto pokemon possui "chave" e $valor", substituindo os termos com $ pelos valores correspondentes ao conjunto chave/valor.

//### 3 - Crie duas variáveis do tipo Number de valores iniciais distintos. Imprima na tela o resultado das operações aritméticas entre elas(+, -, /, *).

//### 4 - Depois disso. Imprima na tela o resultado das operações de comparação maior que (>), menor que(<) e igual(===) para as duas variáveis.

const pokemon = {
    nome: 'Pikachu',
    estamina: 30,
    defesa: 12,
    ataque: 21,
    habilidade: 'Choque do trovão'
};

console.log(`Meu objeto pokemon possui nome:${pokemon.nome}`);
console.log(`Meu objeto pokemon possui estamina:${pokemon.estamina}`);
console.log(`Meu objeto pokemon possui defesa:${pokemon.defesa}`);
console.log(`Meu objeto pokemon possui ataque:${pokemon.ataque}`);
console.log(`Meu objeto pokemon possui habilidade:${pokemon.habilidade}`);


let var1 = 133;

let var2 = 45;

console.log(`Suas operações de adição: ${var1 + var2}`);
console.log(`Suas operações de subtração: ${var1 - var2}`);
console.log(`Suas operações de subtração: ${var1 / var2}`);
console.log(`Suas operações de adição: ${var1 * var2}`);

num1 = '123';
num2 = 123;
console.log(num1 == num2);
console.log(num1 === num2);