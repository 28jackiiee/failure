let interestsValue = document.getElementById('interestsText');
document.querySelector('form.interests').addEventListener('submit', function (e) {

    //prevent the normal submission of the form
    e.preventDefault();

    console.log(interestsValue.value);    
});