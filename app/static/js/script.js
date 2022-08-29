function myfunc(input_rate) {
    var stone = document.getElementById('input_stone');
    stone.value = ((input_rate.value * 100) / 5.5) | 0; 
    console.log(stone.value)
  }

function final_total(rate) {
    var qty = document.getElementById('qty').value; 
    var total = document.getElementById('total');
    total.value = (qty * rate.value)
}