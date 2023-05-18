document.getElementById("left-search").addEventListener("input", function() {
  var LeftSearchTerm = this.value.toLowerCase();
  var LeftSearchItems = document.querySelectorAll(".left-list li");
  LeftSearchItems.forEach(function(item) {
    var LeftName = item.textContent.toLowerCase();
    if (LeftName.includes(LeftSearchTerm)) {
      item.style.display = "block";
    } else {
      item.style.display = "none";
    }
  });
});

function HideLeftBoard(leftBoard, rightBoard) {
  leftBoard.style.display = "none";
  rightBoard.style.display = "block";
}
function ShowLeftBoard(leftBoard, rightBoard) {
  leftBoard.style.display = "block";
  rightBoard.style.display = "none";
}


document.getElementById("left-list-icon").addEventListener("click", function() {
  leftBoard = document.getElementById("left-board");
  rightBoard = document.getElementById("right-board");
  if (leftBoard.style.display === "none" || leftBoard.style.display === "") {
    ShowLeftBoard(leftBoard, rightBoard);
  } else {
    HideLeftBoard(leftBoard, rightBoard);
  }
});


function toggleLeftBoard() {
  const leftBoard = document.getElementById("left-board");
  const rightBoard = document.getElementById("right-board");
  const screenWidth = window.innerWidth;

  if (screenWidth >= 768) {
    // Show the left-board
    leftBoard.style.display = "block";
    rightBoard.style.display = "block";
  } else {
    // Hide the left-board
    leftBoard.style.display = "none";
    rightBoard.style.display = "block";
  }
}

// Initial toggle when the page loads
toggleLeftBoard();

// Toggle when the screen is resized
window.addEventListener("resize", toggleLeftBoard);

