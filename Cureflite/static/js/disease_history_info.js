function changePage(pageNumber) {
  // Make an AJAX request to fetch the new page content
  // You can use any method of your choice to fetch the content
  // For simplicity, let's assume the content is returned as a JSON object

  // Replace the following code with your AJAX request
  // const url = `/api/history?page=${pageNumber}`;
  // fetch(url)
  //   .then(response => response.json())
  //   .then(data => {
  //     // Update the page content with the new data
  //     updatePageContent(data);
  //   })
  //   .catch(error => {
  //     console.error('Error:', error);
  //   });

  // Sample data for demonstration purposes
  const data = {
    page: pageNumber,
    history: [
      { id: 1, title: 'History 1' },
      { id: 2, title: 'History 2' },
      { id: 3, title: 'History 3' },
      // ...
    ]
  };

  // Update the page content with the new data
  updatePageContent(data);
}

function updatePageContent(data) {
  const historyList = document.getElementById('history-list');
  historyList.innerHTML = ''; // Clear the existing content

  // Iterate over the history data and create the list items
  data.history.forEach(history => {
    const listItem = document.createElement('li');
    listItem.textContent = history.title;
    historyList.appendChild(listItem);
  });
}

// Example usage: Change to page 2
changePage(2);