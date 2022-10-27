//task 13

const book = {
    title: 'Battlefield of the mind',
    description: 'Winning the battle in your mind',
    numberOfPage: 117,
    authour: 'Joyce Meyer',
    reading: false,
    toggleOPenAndClose:function(){
        if(book.reading===true){
            book.reading=false
        }else {
            book.reading=true
        }
    }
}

book.toggleOPenAndClose
console.log(book.reading)