
// we get the value of the country and store it 
let countrySelected = $('#id_default_country').val();
// country selected is false then color grey
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
// on every change we get the value of it
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});