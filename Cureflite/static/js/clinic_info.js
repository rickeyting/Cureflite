const firstBoardItems = document.querySelectorAll('.first-board .remove-content a');
firstBoardItems.forEach(item => {
    item.addEventListener('click', () => {
        const itemId = item.classList[0].split('-')[1];
        console.log(item.style.display)
        item.style.display = 'none'; // Hide clicked item in first board
        const inputField = document.querySelector(`input[name="diseases"][value="${itemId}"]`);
        if (inputField) {
            inputField.remove(); // Remove corresponding hidden input field
        }
        const secondBoardItem = document.querySelector(`.second-board .add-${itemId}`);
        if (secondBoardItem) {
            secondBoardItem.style.display = ''; // Show corresponding item in second board
        }
    });
});

const secondBoardItems = document.querySelectorAll('.second-board .add-content a');
secondBoardItems.forEach(item => {
    item.addEventListener('click', () => {
        const itemId = item.classList[0].split('-')[1];
        item.style.display = 'none'; // Hide clicked item in first board
        const firstBoardItems = document.querySelector(`.first-board .remove-${itemId}`);
        const inputField = document.createElement('input');
        inputField.setAttribute('type', 'hidden');
        inputField.setAttribute('name', 'diseases');
        inputField.setAttribute('value', itemId);
        document.getElementById('remove-content').appendChild(inputField);
        if (firstBoardItems) {
            firstBoardItems.style.display = ''; // Show corresponding item in second board
        }
    });
});