const documentoIdentidade = {
    nome: 'Daniel',
    sobrenome: 'Porto',
    cpf: '111.111.111-11',
    empresa: 'Hashtag',
    idade: 29
};

console.log(documentoIdentidade.nome);
console.log(documentoIdentidade['cpf']);


const investimentoMensal = [1000, 2000, 3000, 4000];

console.log(`O valor investido no mês de Janeiro foi de: ${investimentoMensal[0]}`);

let valor1 = undefined;

console.log(valor1);
console.log(typeof valor1);

//undefined esquecimento de variavel
//null foi colocado ali

console.log('------Next------')

let musica = {
    nome: 'Let it Be',
    artista: 'Beatles',
    album: 'Let it Be'
};

let listaDeBandas = ['Beatles', 'Rolling Stones', 'Led zeppelin', 'Cássia Eller', 'Chico Buarque'];

console.log(listaDeBandas[-1]);
listaDeBandas[5] = 'Pitty';
console.log(listaDeBandas[5]);

musica.album = 'Shining';

console.log(musica)

musica.ano = 1969;
console.log(musica);

//Tipo referência = a variável não vai armazenar o dado especificamente e sim a chave 
//variáveis que abrigam obg, array são variáveis com tipos de referência

//const pode modificar os dados de um objeto, mas não podemos jogar um novo objeto

const listaAlunos = ['Daniel', 'Lira', 'Alon'];
listaAlunos[3] = 'Renan';

console.log(listaAlunos);

console.log('Erro');

//listaAlunos = ['Afonso'];
//da erro, pois tentei atribuir uma nova lista, um novo array

