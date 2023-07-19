13.
 const books = {
        title: 'I Saw Heaven',
        description: 'Spiritual',
        numberOfPages: 143,
        authour: 'Robert Liardon',
        reading: false,
        toggleReadingStatus: function(){
            if(books.reading === true){
                books.reading = true
            }else {
                books.reading = false
            }
        }

    }

    console.log(books.reading)