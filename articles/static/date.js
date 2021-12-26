var date = document.querySelector('#date')

let d = new Date();
let day = d.getDate()
let month = d.getMonth()+1
let year = d.getFullYear()

date.innerHTML = `${day}/${month}/${year}`

// --------------------------------------------------------------

var sun = document.querySelector('#sun')
var hr = d.getHours()
var mn = d.getMinutes()

if(hr > 19 || hr < 6){
    sun.innerHTML = '<i class="fas fa-moon"></i>'
}
else{
    sun.innerHTML = '<i class="fas fa-sun"></i>'
}