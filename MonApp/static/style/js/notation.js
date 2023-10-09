$(document).ready(function() {
    const starContainer = $('.star-container');
    const stars = starContainer.find('.star');
    const ratingField = $('#id_note'); // Champ du formulaire où vous stockez la note

    stars.mouseover(function() {
      const index = stars.index(this);
      highlightStars(index + 1);
    });

    starContainer.mouseleave(function() {
      const currentValue = ratingField.val();
      highlightStars(currentValue);
    });

    stars.click(function() {
      const index = stars.index(this) + 1;
      ratingField.val(index);
      highlightStars(index);
    });

    function highlightStars(index) {
      stars.each(function(i) {
        if (i < index) {
          $(this).addClass('filled');
        } else {
          $(this).removeClass('filled');
        }
      });
    }
  });
