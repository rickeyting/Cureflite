// Define the page number and items per page
let userPageNumber = 1;
const userItemsPerPage = 3;

// Get the list element, the previous/next buttons, and the search input
const userList = document.getElementById("all-user");
const userPreviousBtn = document.getElementById("user-previous-btn");
const userNextBtn = document.getElementById("user-next-btn");
const userPageNumberElement = document.getElementById("user-page-number");
const userSearchInput = document.getElementById("email-search-input");
const searchAllCheckbox = document.getElementById("search_all");

// Define a function to update the list items based on the current page number and search query
const updateUserList = () => {
  // Get all the list items
  let items = userList.querySelectorAll(".user-item");

  // Filter the items based on the search query
  const searchQuery = userSearchInput.value.trim().toLowerCase();

  // Calculate the start and end index of items to show on the current page
  const startIndex = (userPageNumber - 1) * userItemsPerPage;
  const endIndex = startIndex + userItemsPerPage;
  const showAll = searchAllCheckbox.checked;

  // Loop through all the items and hide/show them based on the current page and search query
  let i = 0;
  for (let j = 0; j < items.length; j++) {
    const item = items[j];
    const email = item.querySelector(".user-mail").textContent.trim().toLowerCase();
    const isStaff = item.classList.contains("staff");

    if ((showAll || isStaff) && email.includes(searchQuery)) {
      if (i >= startIndex && i < endIndex) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
      i++;
    } else {
      item.style.display = "none";
    }
  }

  // Update the page number display
  const totalPages = Math.ceil(i / userItemsPerPage);
  userPageNumberElement.textContent = `${userPageNumber} of ${totalPages}`;
};

// Add event listeners to the search input, previous button, and next button
userSearchInput.addEventListener("input", () => {
  userPageNumber = 1;
  updateUserList();
});

userPreviousBtn.addEventListener("click", () => {
  if (userPageNumber > 1) {
    userPageNumber--;
    updateUserList();
  }
});

// Add event listener to the "searchAllCheckbox" element
searchAllCheckbox.addEventListener("change", () => {
  // Call the updateUserList function to update the list based on the checkbox value
  updateUserList();
});


userNextBtn.addEventListener("click", () => {
  const items = userList.querySelectorAll(".user-mail");
  const searchQuery = userSearchInput.value.trim().toLowerCase();
  let filteredItems = items;
  if (searchQuery !== "") {
    filteredItems = Array.from(items).filter(item => item.querySelector(".user-mail").textContent.trim().toLowerCase().includes(searchQuery));
  }
  const totalPages = Math.ceil(filteredItems.length / userItemsPerPage);

  if (userPageNumber < totalPages) {
    userPageNumber++;
    updateUserList();
  }
});

// Show the first page of items
updateUserList();