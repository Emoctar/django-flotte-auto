
const texts = ["Maintenant ","C'est facile pour vous","De réserver une voiture"];
let textIndex = 0;
let charIndex = 0;
let isAdding = true;

function animateText() {
    const currentText = texts[textIndex];
    const currentElement = document.getElementById(`animated-text${textIndex + 1}`); // Utilisation correcte des guillemets inversés
    
    if (isAdding) {
        currentElement.textContent = currentText.slice(0, charIndex);
        charIndex++;

        if (charIndex > currentText.length) {
            if (textIndex < texts.length - 1) {
                textIndex++;
                charIndex = 0;
                setTimeout(animateText, 1000); // Pause avant d'aller au texte suivant
                return;
            }

            isAdding = false;
            setTimeout(animateText, 2000); // Pause avant de commencer à supprimer le texte
            return;
        }
    } else {
        currentElement.textContent = currentText.slice(0, charIndex);
        charIndex--;

        if (charIndex === 0) {
            if (textIndex > 0) {
                textIndex--;
                charIndex = texts[textIndex].length;
                setTimeout(animateText, 1000); // Pause avant de retourner au texte précédent
                return;
            }

            isAdding = true;
            setTimeout(animateText, 1000); // Pause avant de recommencer à taper le texte
            return;
        }
    }

    const randomSpeed = 100 + Math.random() * 100;
    setTimeout(animateText, isAdding ? randomSpeed : 50);
}

document.addEventListener('DOMContentLoaded', () => {
    animateText(); // Commencez l'animation une fois que le document est chargé
});


 $(document).ready(function(){
        $(".owl-carousel").owlCarousel({
            items: 4,
            loop: true,
            margin: 15,
            autoplay: true,
            autoplayTimeout: 3000, // Délai entre les transitions en millisecondes
            responsiveClass:true,
            responsive:{
                0:{
                    items:1,
                },
                600:{
                    items:2,
                },
                1000:{
                    items:4,
                }
            }
        })
    });

