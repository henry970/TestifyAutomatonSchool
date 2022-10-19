//task14

const books = [
    {
        title:'Power of your mind',
        description:'put your mind power to work',
        numberOfPage:240,
        author:'pastor Christ',
        reading: true
    },
    {
        title: 'Battlefield of the mind',
        description:'Winning battle in your mind',
        numberOfPage:117,
        author:'Joyce Meyer',
        reading: true
    },
    {
        title:'You can if you think you can',
        description:'All the resource you need are in your mind',
        numberOfPage:297,
        author:'Norman Vincent',
        reading:false
    }
]
for(let key in books ) {
    if(books[key].reading === true) {
        console.log(key,books[key]);
    }
}