function openChangePassword() {
  document.getElementById("ChangePasswordPopup").style.display = "block";
  document.body.classList.add("modal-open");
}

function closeChangePassword() {
  document.getElementById("ChangePasswordPopup").style.display = "none";
}

document.getElementById('photo-upload').addEventListener('change', function(event) {
  var reader = new FileReader();
  reader.onload = function(e) {
    document.getElementById('photo-preview').src = e.target.result;
  };
  reader.readAsDataURL(event.target.files[0]);
});







