function reverseArray(a) {

    let ponteiroMenor = 0;
    let ponteiroMaior = a.lenght -1;

    while(ponteiroMenor < ponteiroMaior) {

        //swap
        let tmp = a[ponteiroMenor];
        a[ponteiroMenor]= a[ponteiroMaior];
        a[ponteiroMaior] = tmp;

        ponteiroMenor++;
        ponteiroMaior--;
    }

}