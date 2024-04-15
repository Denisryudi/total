


function pegarComanda() {

    for(i = 0; i < 3; i++) {
        console.log('Olá, boa noite!');
        console.log('Pegue aqui sua comanda!')
        console.log('Bom apetite!')
    }
}

pegarComanda();

for(i = 0; i < 10;i++) {
    let numeroDaVez = 1;

}


function numerinhoDaVez() {
    c = 0;
    let numeroDaVez = 1;
    while(c < 10) {
        console.log(`O número da vez é o ${numeroDaVez} ao quadrado vale ${numeroDaVez ** 2}`)
        numeroDaVez += 1;
        c++;

    }
}

numerinhoDaVez();
                            //parâmetro
function calcularQuadrado(numeroDaVez1) {
    console.log(`O número da vez é o ${numeroDaVez1}`);
    console.log(`O número da vez é o ${numeroDaVez1} ao quadrado vale ${numeroDaVez1 ** 2}`);
}
         //argumento = 2
calcularQuadrado(2)