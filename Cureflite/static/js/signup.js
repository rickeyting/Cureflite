const staffStatusCheckbox = document.getElementById('staffStatusCheckbox');
const jobTitleInput = document.getElementById('jobTitleInput');

staffStatusCheckbox.addEventListener('change', function() {
    jobTitleInput.style.display = this.checked ? 'flex' : 'none';
});

document.getElementById('photo-upload').addEventListener('change', function(event) {
  var reader = new FileReader();
  reader.onload = function(e) {
    document.getElementById('photo-preview').src = e.target.result;
  };
  reader.readAsDataURL(event.target.files[0]);
});