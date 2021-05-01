// get left and right arrows
var leftBtn = document.getElementById('left-arrow');
var rightBtn = document.getElementById('right-arrow');

// find all 8 event cards
var eventCards = document.getElementsByClassName('event-card');

function scroll(d){
    // slide cards left and right and disables buttons when content is over
    // this function assumes that there is only 8 event cards and 4 on the screen
    // TODO: make this work for any number of number of cards
    // TODO: make transition smoother
    var n;
    try {
    // returns buttons to initial active state
    leftBtn.classList.remove('disabled');
    rightBtn.classList.remove('disabled');

    // find index of first visible event card 
    for (n = 0; n < eventCards.length - 3; n++) {
        const style = getComputedStyle(eventCards[n], 'display')
        if (style.display == "block") {
            break;
        };
    };
    // display and hide cards depending on the button clicked
    if (d == 'right') {
        eventCards[n+4].style.display = 'block';
        eventCards[n].style.display = 'none';
        if (n == 3) {
            // this means there are no cards to the right anymore
            rightBtn.classList.toggle('disabled');
        }
    } else {
        eventCards[n-1].style.display = 'block';
        eventCards[n+3].style.display = 'none';
        if (n == 1) {
            // this means there are no cards to the left anymore
            leftBtn.classList.toggle('disabled');
        }
    };

    } catch(err) {
        // in case the user keeps clicking the disabled button
        if (n == 0) {
            leftBtn.classList.toggle('disabled');
        } else if (n == 4 ) {
            rightBtn.classList.toggle('disabled');
        }
    }
    
};

leftBtn.addEventListener("click", function() {scroll('left');})
rightBtn.addEventListener("click", function() {scroll('right');})