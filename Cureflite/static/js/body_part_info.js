const firstBoardItems = document.querySelectorAll('.first-board .remove-content a');
firstBoardItems.forEach(item => {
    item.addEventListener('click', () => {
        const itemId = item.getAttribute('symptom-group-id');
        const itemName = item.textContent.trim();
        item.style.display = 'none'; // Hide clicked item in first board
        const group_inputField = document.querySelector(`input[name="group"][value="${itemId}"]`);
        if (group_inputField) {
            group_inputField.remove(); // Remove corresponding hidden input field
        }
        const secondBoardItem = document.querySelector(`.second-board a[symptom-group-id="${itemId}"]`);
        if (secondBoardItem) {
            secondBoardItem.style.display = ''; // Show corresponding item in second board
        }
        const thirdBoardItem = document.querySelector(`.third-board a[symptom-group-id="${itemId}"]`);
        if (thirdBoardItem) {
            thirdBoardItem.style.display = ''; // Show corresponding item in second board
        }
    });
});

const secondBoardItems = document.querySelectorAll('.second-board .add-content a, .third-board .add-content a');
secondBoardItems.forEach(item => {
    item.addEventListener('click', () => {
        const itemId = item.getAttribute('symptom-group-id');
        const itemName = item.textContent.trim();
        console.log(itemId, itemName)
        item.style.display = 'none'; // Hide clicked item in first board
        const firstBoardItems = document.querySelector(`.first-board a[symptom-group-id="${itemId}"]`);
        const inputField = document.createElement('input');
        inputField.setAttribute('type', 'hidden');
        inputField.setAttribute('name', 'group'); // Set 'name' attribute to 'group'
        inputField.setAttribute('value', itemId);
        document.getElementById('remove-content').appendChild(inputField);
        // add option
        const newOption = document.createElement('option');
        if (firstBoardItems) {
            firstBoardItems.style.display = ''; // Show corresponding item in second board
        }
    });
});