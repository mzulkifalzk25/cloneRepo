
/* Add to cart function */
$(document).ready(function() {
    $('.add-to-cart-form').submit(function(e) {
      e.preventDefault();
      let form = $(this);
      let product_id = form.find('input[name="product_id"]').val();
      let quantity = form.find('input[name="quantity"]').val();


      $.ajax({
        type: 'POST',
        url: '/add_to_cart/',
        data: {
          'product_id': product_id,
          'quantity': quantity,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response) {
          alert('Item added to cart!');
        },
        error: function(response) {
          alert('You have to Log In to add to cart.');
        }
      });
    });
  });

  /* copyright year function */

  const currentYear = new Date().getFullYear();
  const yearSpan = document.getElementById('currentYear');
  yearSpan.textContent = currentYear;



