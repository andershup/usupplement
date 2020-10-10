/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
// variables camel cased for consistency with python
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1); // script elements contain their value so .text() to retrieve
var clientSecret = $('#id_client_secret').text().slice(1, -1); // slice to get rid of the quotation marks
var stripe = Stripe(stripePublicKey); // stripe script in base template so to set up stripe just need create variable using the strope public key.
var elements = stripe.elements(); // create an instance of stripe elements 
var style = { //card elements can accept style. Also from stripe doc
    base: {
        color: '#A52A2A',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545', //bootstraps danger class color
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style}); //not sure it style is added here or on the mount.
card.mount('#card-element'); // mount it to the elemnt in checkout.html

/* Handle realtime validation errors on the card element
   Copied from Code Institute source code
   The "Your card is not valid message */
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit from Stripe 
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // Preventing the default action of POST
    ev.preventDefault();
    // Disable both card element and submit to avoid multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // fade out the form when user clicks submit
    //$('#payment-form').fadeToggle(100); THESE ARE NOT FUNCTIONING
    //$('#loading-overlay').fadeToggle(100);
    // Stripe method to send card info securely to stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card, //Provide to card to stripe. This is where weghooks start
            // we need to stuff the order details into here so we can get it from paymentintent success when comes back from stripe
            // stripe payment intent object has a spot for a billing details object called billing details.
                    billing_details: {
                    name: $.trim(form.full_name.value), // trip off any eccess white space
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: { //all the same fields except email
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    // only adding postcode here. billing will come form stripe and stripe will override it there.
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },

        //Then execute this function on the result
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Disable the fadetoggles from above
            //$('#payment-form').fadeToggle(100);      THESE ARE NOT FUNCTIONING
            //$('#loading-overlay').fadeToggle(100);
            //If there is an error we disabled to false to allow the user to fix it
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
