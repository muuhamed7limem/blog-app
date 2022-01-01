var title = document.querySelector('input[name=title]')
var slug = document.querySelector('input[name=slug]')
var pp = document.querySelector('.warn')


function slugify(val){

    return val.toString().toLowerCase().trim()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/&/g, '-and-')         // Replace & with 'and'
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-');        // Replace multiple - with single -
}


title.addEventListener('keyup' , function(){

    slug.value = `${slugify(title.value)}${Math.floor(Math.random() * (9999999999 - 1000000000 + 1) + 1000000000)}`
})

// ====================================================

title.onclick = function(){
    pp.style.display = 'grid'
}

title.onkeyup = function(){
    pp.style.display = 'none'
}