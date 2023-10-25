function mru($d, $t){  
    return ($d[1] - $d[0]) / $t

}

function main(){
    var di = 0; //metros
    var df = 80; //metros
    var t = 40; //segundos

    let d = [di,df]
    const vm = mru(d, t);

    console.log(vm, `m/s`);
}
main()