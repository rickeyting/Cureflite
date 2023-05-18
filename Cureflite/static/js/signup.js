const staffStatusCheckbox = document.getElementById('staffStatusCheckbox');
const jobTitleInput = document.getElementById('jobTitleInput');

staffStatusCheckbox.addEventListener('change', function() {
    jobTitleInput.style.display = this.checked ? 'flex' : 'none';
});