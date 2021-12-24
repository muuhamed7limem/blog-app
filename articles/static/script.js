var title = document.querySelector('input[name=title]')
var slug = document.querySelector('input[name=slug]')


function slugify(val){

    return val.toString().toLowerCase().trim()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/&/g, '-and-')         // Replace & with 'and'
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-');        // Replace multiple - with single -
}


title.addEventListener('keyup' , function(){

    slug.value = slugify(title.value)
})