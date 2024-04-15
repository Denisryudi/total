function resolverBhaskara() {}


function calcularRaizQuadrada(base) {
    return base**(1/2);

}

calcularRaizQuadrada();

//return = bomba codificada

function criarPessoa(nome, idade) {
    return { nome: nome, idade: idade };
}

const pessoa = criarPessoa('João', 25);
console.log(pessoa);