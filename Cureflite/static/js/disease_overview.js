function submitForm() {
    document.getElementById("myForm").submit();
    showSpinner();
  }

document.getElementById("left-search").addEventListener("input", function() {
  var LeftSearchTerm = this.value.toLowerCase();
  var LeftSearchItems = document.querySelectorAll(".disease-list li");

  LeftSearchItems.forEach(function(item) {
    var LeftName = item.textContent.toLowerCase();
    if (LeftName.includes(LeftSearchTerm)) {
      console.log(item);
      item.style.display = "flex";
    } else {
      item.style.display = "None";
    }
  });
});





