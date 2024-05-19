// depndent
function toggle(){
    var blur = document.getElementById('blur')
    blur.classList.toggle('active')

    var popup = document.getElementById('popup')
    popup.classList.toggle('active')
}
   // for cistomer
function pop(){
   var blu = document.getElementById('CS')
   blu.classList.toggle('active')

   var show = document.getElementById('ping')
   show.classList.toggle('active')
}
// for claim
function view(){
   var yamete = document.getElementById('claim')
   yamete.classList.toggle('active')

   var give = document.getElementById('popup2')
   give.classList.toggle('active')
}
// four popup
function view1(){
   var onichan = document.getElementById('claim2')
   onichan.classList.toggle('active')

   var naruto = document.getElementById('popup3')
   naruto.classList.toggle('active')
}

    // for claim
//     function toggle(){
//     var blur = document.getElementById('blur')
//     blur.classList.toggle('active')

//     var popup = document.getElementById('popup')
//     popup.classList.toggle('active')
// }


// function addContact(){
//     temp="<input type='search' value=''.      alt='clear' >"; 
//    var contact_added=document.getElementById("text_name").value; 
//    var contact=document.getElementById("no").value;
//     document.getElementById("text_name").value=contact+temp+contact_added;
//     }
//     contacts=[];
// function addContact(){
//          newcontact=document.getElementById("no");    
// contacts.push(newcontact.value);
// newcontact.value="";   
// render();
// }

// function delta(i){
// contacts.splice(i,1);
// render();
// }
// //this takes the contacts array and adds it to the page + hidden submit field
// function render(){
//     hidden=document.getElementById("contacts_hidden");
// all=document.getElementById("contacts");
// content="";
// for(i=0;i<contacts.length;i++){
// //add a delete button
// content+=contacts[i]+"<a href='javascript:delta("+i+")'>Delete</a>";
// }
// all.innerHTML=content;
// hidden.value=contacts.join(";");
// }
// $(document).ready(function(){
//     $( ".add-row" ).click(function(){
//        var $clone = $( "ul.personal-details" ).first().clone();
//        $clone.append( "<button type='button' class='remove-row'>-</button>" );
//        $clone.insertBefore( ".add-row" );
//     });
   
//     $( ".form-style-9" ).on("click", ".remove-row", function(){
//        $(this).parent().remove();
//     });
//  });

// DropDown

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
// function myFunction() {
   // document.getElementById("myDropdown").classList.toggle("show");
//  }
 
 // Close the dropdown menu if the user clicks outside of it
//  window.onclick = function(event) {
   // if (!event.target.matches('.icons')) {
   //   var dropdowns = document.getElementsByClassName("dropdown-content");
   //   var i;
   //   for (i = 0; i < dropdowns.length; i++) {
      //  var openDropdown = dropdowns[i];
      //  if (openDropdown.classList.contains('show')) {
         // openDropdown.classList.remove('show');
      //  }
   //   }
   // }
//  }
// const openModelButtons = document.querySelectorAll('[data-model-target]')
// const closeModelButtons = document.querySelectorAll('[data-close-button]')
// const overlay = document.getElementById('overlay')


// overlay.addEventListener('click',() => {
//    const moals = document.querySelectorAll('.model.active')
//    model.forEach(model => {
//       closeModel
//    })
// })

// openModelButtons.forEach(button => {
//    button.addEventListener('click',() =>{
//       const model =document.querySelector(button.dataset.modelTarget)
//       openModel(model)
//    })
// })



// closeModelButtons.forEach(button => {
//    button.addEventListener('click',() =>{
//       const model = button.closest('.model')
//       closeModel(model)
//    })
// })
// function openModel(model){
//    if (model == null) return
//    model.classList.add('active')
//    overlay.classList.add('active')
// }
// function openModel(model){
//    if (model == null) return
//    model.classList.remove('active')
//    overlay.classList.remove('active')
// }