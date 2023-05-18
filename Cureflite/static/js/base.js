function openLoginForm() {
  document.getElementById("loginPopup").style.display = "block";
  document.body.classList.add("modal-open");
  closeForgotForm()
}


function openForgotForm() {
  document.getElementById("forgotPopup").style.display = "block";
  document.body.classList.add("modal-open");
  closeLoginForm()
}


function closeLoginForm() {
    document.getElementById("loginPopup").style.display = "none";
}

function closeForgotForm() {
    document.getElementById("forgotPopup").style.display = "none";
}


var modal_login = document.getElementById("loginPopup");
var modal_forgot = document.getElementById("forgotPopup");
var modalChange = document.getElementById("ChangePasswordPopup");

// When the user clicks anywhere outside of a modal, close it
window.onclick = function(event) {
  if (event.target == modal_login) {
    modal_login.style.display = "none";
  } else if (event.target == modal_forgot) {
    modal_forgot.style.display = "none";
  } else if (event.target == modalChange) {
    modalChange.style.display = "none";
  }
}

function showSpinner() {
  $('#spinnerOverlay').removeClass('hide');
}

// Hide the spinner overlay
function hideSpinner() {
  $('#spinnerOverlay').addClass('hide');
}


document.addEventListener('readystatechange', function() {
  if (document.readyState === 'complete') {
    // Document has finished loading
    hideSpinner();
    // Perform actions here
  } else {
    // Document is still loading
    showSpinner();
    // Perform actions here
  }
});

$(document).keyup(function(e) {
     if (e.keyCode == 27) {
        hideSpinner();
    }
});