function mru($d, $t) {
  return ($d[1] - $d[0]) / $t;
}
function main() {
  var di = 0;
  var df = 80;
  var t = 40;
  var d = [di, df];
  let vm = mru(d, t);
  console.log(vm, `m/s`);
}
main();
