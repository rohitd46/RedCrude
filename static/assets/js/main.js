$(window).on('load', function() {
    setTimeout(function() {
        $(".preloader").delay(300).fadeOut(400);
    });
});
// data table
$('.default-datatable').DataTable({
    responsive: true,
    "bLengthChange": true,
    "ordering": true,
    "orderClasses": true,
    'stripeClasses': ['', 'stripe'],
    "info": true,
    "paging": true,
});
// $('.dataTables_length').removeClass('form-control');
var table = $('.default-datatable').DataTable();
//DataTable custom search field
$('#custom-filter').keyup(function() {
    table.search(this.value).draw();
});
// ################### start select option #################


var x, i, j, selElmnt, a, b, c;
/*look for any elements with the class "custom-select":*/
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    /*for each element, create a new DIV that will act as the selected item:*/
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    x[i].appendChild(a);
    /*for each element, create a new DIV that will contain the option list:*/
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j = 1; j < selElmnt.length; j++) {
        /*for each option in the original select element,
        create a new DIV that will act as an option item:*/
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function(e) {
            /*when an item is clicked, update the original select box,
            and the selected item:*/
            var y, i, k, s, h;
            s = this.parentNode.parentNode.getElementsByTagName("select")[0];
            h = this.parentNode.previousSibling;
            for (i = 0; i < s.length; i++) {
                if (s.options[i].innerHTML == this.innerHTML) {
                    s.selectedIndex = i;
                    h.innerHTML = this.innerHTML;
                    y = this.parentNode.getElementsByClassName("same-as-selected");
                    for (k = 0; k < y.length; k++) {
                        y[k].removeAttribute("class");
                    }
                    this.setAttribute("class", "same-as-selected");
                    break;
                }
            }
            h.click();
        });
        b.appendChild(c);
    }
    x[i].appendChild(b);
    a.addEventListener("click", function(e) {
        /*when the select box is clicked, close any other select boxes,
        and open/close the current select box:*/
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
    });
}

function closeAllSelect(elmnt) {
    /*a function that will close all select boxes in the document,
    except the current select box:*/
    var x, y, i, arrNo = [];
    x = document.getElementsByClassName("select-items");
    y = document.getElementsByClassName("select-selected");
    for (i = 0; i < y.length; i++) {
        if (elmnt == y[i]) {
            arrNo.push(i)
        } else {
            y[i].classList.remove("select-arrow-active");
        }
    }
    for (i = 0; i < x.length; i++) {
        if (arrNo.indexOf(i)) {
            x[i].classList.add("select-hide");
        }
    }
}
/*if the user clicks anywhere outside the select box,
then close all select boxes:*/
document.addEventListener("click", closeAllSelect);

// ################### end select option #################

$('select .auto-width-select').change(function() {
        var text = $(this).find('option:selected').text()
        var $aux = $('<select/>').append($('<option/>').text(text))
        $(this).after($aux)
        $(this).width($aux.width())
        $aux.remove()
    }).change()
    // ####### start wow animtion effects ###################
var wow = new WOW({
    boxClass: 'wow', // animated element css class (default is wow)
    animateClass: 'animated', // animation css class (default is animated)
    offset: 0, // distance to the element when triggering the animation (default is 0)
    mobile: true, // trigger animations on mobile devices (default is true)
    live: true, // act on asynchronously loaded content (default is true)
    callback: function(box) {
        // the callback is fired every time an animation is started
        // the argument that is passed in is the DOM node being animated
    },
    scrollContainer: null // optional scroll container selector, otherwise use window
});
wow.init();
// ####### end wow animtion effects ###################
/*===================================*
      start window scroll
  /*===================================*/
$(window).on('scroll', function() {
    var scroll = $(window).scrollTop();
    var scroll2 = $(window).scrollTop();

    if (scroll >= 250) {
        $('.cover-navbar').addClass('nav-sticky');
    } else {
        $('.cover-navbar').removeClass('nav-sticky');
    }

    if (scroll2 >= 250) {
        $('.cover-navbar2').addClass('nav-fixed');
    } else {
        $('.cover-navbar2').removeClass('nav-fixed');
    }

});
/*===================================*
        end window scroll
    /*===================================*/
// ################### start team members #################

VanillaTilt.init(document.querySelectorAll(".title-effect"), {
    max: 10,
    speed: 400
});
// ################### end team members #################\

$(".whishbutton").click(function() {
    $(this).toggleClass("heartactive");
});


// check for saved 'RedcrudeDark' in localStorage
let RedcrudeDark = localStorage.getItem('RedcrudeDark');

const RedcrudeDarkToggle = document.querySelector('#dark-mode-toggle');

const enableDarkMode = () => {
    // 1. Add the class to the body
    document.body.classList.add('darkmodeclass');
    // 2. Update RedcrudeDark in localStorage
    localStorage.setItem('RedcrudeDark', 'enabled');
}

const disableDarkMode = () => {
    // 1. Remove the class from the body
    document.body.classList.remove('darkmodeclass');
    // 2. Update RedcrudeDark in localStorage 
    localStorage.setItem('RedcrudeDark', null);
}

// If the user already visited and enabled RedcrudeDark
// start things off with it on
if (RedcrudeDark === 'enabled') {
    enableDarkMode();
    $('#dark-mode-toggle').prop("checked", true)
}

// When someone clicks the button
RedcrudeDarkToggle.addEventListener('click', () => {
    // get their RedcrudeDark setting
    RedcrudeDark = localStorage.getItem('RedcrudeDark');

    // if it not current enabled, enable it
    if (RedcrudeDark !== 'enabled') {
        enableDarkMode();
        // if it has been enabled, turn it off  
    } else {
        disableDarkMode();
    }
});