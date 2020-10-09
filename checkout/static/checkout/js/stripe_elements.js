/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1); // script elements contain their value so .text() to retrieve
var client_secret = $('#id_client_secret').text().slice(1, -1); // slice to get rid of the quotation marks
var stripe = Stripe(stripe_public_key); // stripe script in base template so to set up stripe just need create variable using the strope public key.
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
