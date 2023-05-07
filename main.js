let interestsValue = document.getElementById('interestsText');
document.querySelector('form.interests').addEventListener('submit', function (e) {

    //prevent the normal submission of the form
    e.preventDefault();

    console.log(interestsValue.value);    
});


/*making tag buttons*/
const tagColors = ["#D6EFFF", "#FED18C", "#FEFEFF", "#47E5BC"]
const tags = document.getElementsByClassName("tag");
for(let i=0; i<tags.length; i++){
    tags[i].addEventListener("click", function(){
        console.log(tags[i]);

        tags[i].style.backgroundColor  = tagColors[3];
    })

    tags[i].addEventListener("dblclick", function(){
        tags[i].style.backgroundColor = tagColors[Math.floor(Math.random() * 3)];
    })
}