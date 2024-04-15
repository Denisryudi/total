function mediaAluno(a, b ,c) {
    const x = (a + b + c) /3;
    console.log(`A média desses alunos é: ${x}`);
    return x;
}
mediaAluno(5, 10, 10)

function mediaFinal(a, b, c, d) {
    const mediaAluno1 = mediaAluno(a, b, c);
    const mediaAlunoFinal = (mediaAluno1 + d) /2;
    return mediaAlunoFinal;
}

const mediaFinalFinal = mediaFinal(5, 5, 5, 10);
console.log(mediaFinalFinal);


function somar(a, b) {
    const resultado = a + b;
    return resultado;
}

const resultadoSoma = somar(3, 5);
console.log(resultadoSoma); // Saída: 8

//Ao usar return, você está fornecendo um valor para quem chamou a função. Isso permite que o valor seja utilizado em outras partes do seu programa.
//Ou seja faz um resumo, e torna ele disponivel para quem precisar dele

// OK
function converterParaFarenheit(temperaturaCelsius) {
    const tempFarenheit = (9 / 5) * temperaturaCelsius + 32;
    return tempFarenheit;
}

const calcularFarenheit = converterParaFarenheit(30);
console.log(calcularFarenheit);
// return OK 


//Sem return
function converterParaFarenheit(temperaturaCelsius) {
    const tempFarenheit = (9 / 5) * temperaturaCelsius + 32;
    console.log(
      `a temperatura correspondente em Farenheit é de ${tempFarenheit}ºF`
    );
  }