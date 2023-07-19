14.
const books = [
{
    title: 'I Saw Heaven',
    description: 'Vision About Heaven',
    numberOfPages: 143,
    author: 'Robert Liardon',
    reading: true,
},
{
    title: 'New School Chemistry',
    description: 'Education',
    numberOfPages: 650,
    author: 'Ababio',
    reading: false,
},
{
    title: 'Perfect Testing',
    description: 'Software Testing',
    numberOfPages: 150,
    author: 'Michael Alabi',
    reading: true,
},
{
    title: 'Your food Your Health',
    description: 'Health',
    numberOfPages: 100,
    author: 'Ibironke Yekinni',
    reading: false,
},
{
    title: 'Look befor You Leap',
    description: 'Relatioship',
    numberOfPages: 180,
    author: 'Felicia A',
    reading: false,
},
{
    title: 'Welcome Home',
    description: 'Romatic',
    numberOfPages: 120,
    author: 'Isaac A',
    reading: false,
}

];

for(let i = 0; i<books.length; i++){
    if(books[i].reading === true){
        console.log(books[i])
    }
}