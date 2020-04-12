const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// setTimeout(function() {
//     $('#message').fadeOut('slow');
//     },3000);

/* ---This script is for Cleave.js phone formating---*/
/*https://nosir.github.io/cleave.js/ */

// var webcollection = document.getElementsByClassName("http-prefix");
// var webcol = Array.from(webcollection);
// webcol.forEach(function (wb) {
//     new Cleave(wb, {
//       prefix: 'http://',
//       noImmediatePrefix: true,
//       uppercase: false
//     })
// });

var mydate = document.getElementsByClassName("date-picker");
var mydt = Array.from(mydate);
mydt.forEach(function (md) {
    new Cleave(md, {
        date: true,
        delimiter: '-',
        datePattern: ['Y', 'm', 'd']
    })
});

var phoneCollection = document.getElementsByClassName("format-phone");
var phs = Array.from(phoneCollection);
phs.forEach(function (ph) {
    new Cleave(ph, {
        phone: true,
        delimiter: '-',
        phoneRegionCode: 'CA'
    })
});

/*This is a script to manage country codes */
document.getElementById("selectCountry").addEventListener('change', function (e) {

    var c_code = document.getElementById("selectCountry").value;
    var d_code = ""

    switch (c_code) {
        case "CA":
            d_code = "+1";
            break;
        case "US":
            d_code = "+1";
            break;
        case "UA":
            d_code = "+380";
            break;
        case "FR":
            d_code = "+33";
            break;
        case "RU":
            d_code = "+7";
            break;
        case "PT":
            d_code = "+351";
            break;
        case "AE":
            d_code = "+971";
            break;
        case "DE":
            d_code = "+49";
            break;
        case "IL":
            d_code = "+972";
            break;
        case "PL":
            d_code = "+48";
            break;

        default:
            d_code = "+1";
    }

    document.getElementById("countryCode").value = d_code;
    document.getElementById("countryCode_s").value = d_code;
 
    e.preventDefault();
});