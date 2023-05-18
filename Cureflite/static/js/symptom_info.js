const firstBoardItems = document.querySelectorAll('.first-board .remove-content a');
firstBoardItems.forEach(item => {
    item.addEventListener('click', () => {
        const itemId = item.classList[0].split('-')[1];
        const itemName = item.classList[0].split('-')[2];
        item.style.display = 'none'; // Hide clicked item in first board
        const group_inputField = document.querySelector(`input[name="group"][value="${itemId}"]`);
        const name_options = document.querySelector(`select[name="chinese_name"] option[value="${itemName}"]`);
        if (name_options) {
            name_options.remove(); // Remove corresponding hidden input field
        }
        if (group_inputField) {
            group_inputField.remove(); // Remove corresponding hidden input field
        }
        const secondBoardItem = document.querySelector(`.second-board .add-${itemId}-${itemName}`);
        if (secondBoardItem) {
            secondBoardItem.style.display = ''; // Show corresponding item in second board
        }
        const thirdBoardItem = document.querySelector(`.third-board .add-${itemId}-${itemName}`);
        if (thirdBoardItem) {
            thirdBoardItem.style.display = ''; // Show corresponding item in second board
        }
    });
});

const secondBoardItems = document.querySelectorAll('.second-board .add-content a, .third-board .add-content a');
secondBoardItems.forEach(item => {
    item.addEventListener('click', () => {
        const itemId = item.classList[0].split('-')[1];
        const itemName = item.classList[0].split('-')[2];
        item.style.display = 'none'; // Hide clicked item in first board
        const firstBoardItems = document.querySelector(`.first-board .remove-${itemId}-${itemName}`);
        const inputField = document.createElement('input');
        inputField.setAttribute('type', 'hidden');
        inputField.setAttribute('name', 'group'); // Set 'name' attribute to 'group'
        inputField.setAttribute('value', itemId);
        document.getElementById('remove-content').appendChild(inputField);
        // add option
        const newOption = document.createElement('option');
        newOption.value = itemName;
        newOption.textContent = itemName;
        document.getElementById('chinese_name').appendChild(newOption);
        if (firstBoardItems) {
            firstBoardItems.style.display = ''; // Show corresponding item in second board
        }
    });
});