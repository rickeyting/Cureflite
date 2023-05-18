const selectElement = document.getElementById('clinic-option');
selectElement.addEventListener('change', function() {
  const selectedOption = selectElement.options[selectElement.selectedIndex];
  const selectedClinic = selectedOption.value;

  if (selectedClinic !== '選擇新增') {
    const clinicId = selectedOption.getAttribute('data-clinic-id');
    const clinicName = selectedOption.getAttribute('data-clinic-name');

    // Create the <a> element with the selected clinic
    const newClinicElement = document.createElement('a');
    newClinicElement.setAttribute('data-clinic-id', clinicId);
    newClinicElement.setAttribute('data-clinic-name', clinicName);
    newClinicElement.innerHTML = `${clinicName} <i class="bi bi-dash"></i>`;
    newClinicElement.style.setProperty("margin-right", "5px");
    // Append the <a> element to the remove-content div
    const removeContentDiv = document.querySelector('.remove-content .selected-option');
    removeContentDiv.appendChild(newClinicElement);

    // Append input
    const inputField = document.createElement('input');
    inputField.setAttribute('type', 'hidden');
    inputField.setAttribute('name', 'clinic');
    inputField.setAttribute('value', clinicName);
    removeContentDiv.appendChild(inputField);


    // Remove the selected option from the dropdown
    selectElement.remove(selectElement.selectedIndex);
  }
});

const removeContentDiv = document.querySelector('.selected-option');
removeContentDiv.addEventListener('click', function(event) {
  if (event.target.tagName === 'A') {
    const removedClinicElement = event.target;
    const clinicId = removedClinicElement.getAttribute('data-clinic-id');
    const clinicName = removedClinicElement.getAttribute('data-clinic-name');

    // Remove input
    const inputField = document.querySelector(`input[name="clinic"][value="${clinicName}"]`);
    if (inputField) {
      inputField.remove(); // Remove corresponding hidden input field
    }

    // Create the option element with the removed clinic
    const newOptionElement = document.createElement('option');
    newOptionElement.setAttribute('data-clinic-id', clinicId);
    newOptionElement.setAttribute('data-clinic-name', clinicName);
    newOptionElement.textContent = clinicName;

    // Append the option element to the clinic-option dropdown
    const selectElement = document.getElementById('clinic-option');
    selectElement.appendChild(newOptionElement);

    // Remove the clicked <a> element and its input field
    removedClinicElement.remove();
  }
});

const triggerSymptomDiv = document.querySelector('.selected-symptoms');
triggerSymptomDiv.addEventListener('click', function(event) {
  if (event.target.tagName === 'A') {
    const triggerSymptomElement = event.target;
    const symptomName = triggerSymptomElement.getAttribute('data-symptom-name');
    const activateStatus = triggerSymptomElement.getAttribute('activated');

    // Remove input and change style
    if (activateStatus == "on") {
        triggerSymptomElement.setAttribute('activated', "off");
        const inputField = document.querySelector(`input[name="symptoms"][value="${symptomName}"]`);
        if (inputField) {
          inputField.remove(); // Remove corresponding hidden input field
        }
        triggerSymptomElement.style.border = '1px solid #FF6347';
        triggerSymptomElement.style.backgroundColor = '#FF6347';
        triggerSymptomElement.style.setProperty("text-decoration", "line-through");
        triggerSymptomElement.innerHTML = `${symptomName}<i class="bi bi-dash"></i>`;
        triggerSymptomElement.addEventListener('mouseenter', function() {
          triggerSymptomElement.style.backgroundColor = '#FF6347'; // Set the desired background color on hover
        });
        triggerSymptomElement.addEventListener('mouseleave', function() {
          triggerSymptomElement.style.backgroundColor = ''; // Reset the background color when not hovering
        });
    } else {
        triggerSymptomElement.setAttribute('activated', "on");
        const inputField = document.createElement('input');
        inputField.setAttribute('type', 'hidden');
        inputField.setAttribute('name', 'symptoms');
        inputField.setAttribute('value', symptomName);
        triggerSymptomDiv.appendChild(inputField);
        triggerSymptomElement.style.border = '1px solid #00FA9A';
        triggerSymptomElement.style.backgroundColor = '#00FA9A';
        triggerSymptomElement.style.setProperty("text-decoration", "");
        triggerSymptomElement.innerHTML = `${symptomName}<i class="bi bi-plus"></i>`;
        triggerSymptomElement.addEventListener('mouseenter', function() {
          triggerSymptomElement.style.backgroundColor = '#00FA9A'; // Set the desired background color on hover
        });
        triggerSymptomElement.addEventListener('mouseleave', function() {
          triggerSymptomElement.style.backgroundColor = ''; // Reset the background color when not hovering
        });
    }
  }
});

const triggerBadHabitDiv = document.querySelector('.selected-bad-habits');
triggerBadHabitDiv.addEventListener('click', function(event) {
  if (event.target.tagName === 'A') {
    const triggerBadHabitElement = event.target;
    const badHabitName = triggerBadHabitElement.getAttribute('data-bad_habit-name');
    const activateStatus = triggerBadHabitElement.getAttribute('activated');

    // Remove input and change style
    if (activateStatus == "on") {
        triggerBadHabitElement.setAttribute('activated', "off");
        const inputField = document.querySelector(`input[name="bad_habits"][value="${badHabitName}"]`);
        if (inputField) {
          inputField.remove(); // Remove corresponding hidden input field
        }
        triggerBadHabitElement.style.border = '1px solid #FF6347';
        triggerBadHabitElement.style.backgroundColor = '#FF6347';
        triggerBadHabitElement.style.setProperty("text-decoration", "line-through");
        triggerBadHabitElement.innerHTML = `${badHabitName}<i class="bi bi-dash"></i>`;
        triggerBadHabitElement.addEventListener('mouseenter', function() {
          triggerBadHabitElement.style.backgroundColor = '#FF6347'; // Set the desired background color on hover
        });
        triggerBadHabitElement.addEventListener('mouseleave', function() {
          triggerBadHabitElement.style.backgroundColor = ''; // Reset the background color when not hovering
        });
    } else {
        triggerBadHabitElement.setAttribute('activated', "on");
        const inputField = document.createElement('input');
        inputField.setAttribute('type', 'hidden');
        inputField.setAttribute('name', 'bad_habits');
        inputField.setAttribute('value', badHabitName);
        triggerBadHabitDiv.appendChild(inputField);
        triggerBadHabitElement.style.border = '1px solid #00FA9A';
        triggerBadHabitElement.style.backgroundColor = '#00FA9A';
        triggerBadHabitElement.style.setProperty("text-decoration", "");
        triggerBadHabitElement.innerHTML = `${badHabitName}<i class="bi bi-plus"></i>`;

        triggerBadHabitElement.addEventListener('mouseenter', function() {
          triggerBadHabitElement.style.backgroundColor = '#00FA9A'; // Set the desired background color on hover
        });
        triggerBadHabitElement.addEventListener('mouseleave', function() {
          triggerBadHabitElement.style.backgroundColor = ''; // Reset the background color when not hovering
        });
    }
  }
});

const triggerSymptomElements = document.querySelectorAll('.selected-symptoms a, .selected-bad-habits a');
triggerSymptomElements.forEach(function(element) {
  element.addEventListener('dblclick', function(event) {
    if (event.detail > 1) {
      event.preventDefault();
    }
  });
});


// Symptom section
const symptomInput = document.getElementById('symptom-input');
const selectedSymptomsDiv = document.querySelector('.selected-symptoms');

symptomInput.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault(); // Prevent the form from submitting
    const symptomName = symptomInput.value.trim();
    if (symptomName !== '') {
      const newSymptomElement = document.createElement('a');
      newSymptomElement.setAttribute('data-symptom-name', symptomName);
      newSymptomElement.setAttribute('activated', 'on');
      newSymptomElement.innerHTML = `${symptomName}<i class="bi bi-dash"></i>`;
      newSymptomElement.style.setProperty("margin-right", "5px");

      const newInputField = document.createElement('input');
      newInputField.setAttribute('type', 'hidden');
      newInputField.setAttribute('name', 'symptoms');
      newInputField.setAttribute('value', symptomName);

      selectedSymptomsDiv.appendChild(newSymptomElement);
      selectedSymptomsDiv.appendChild(newInputField);

      symptomInput.value = '';
    }
  }
});

// Bad habit section
const badHabitInput = document.getElementById('bad_habit-input');
const selectedBadHabitsDiv = document.querySelector('.selected-bad-habits');

badHabitInput.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault(); // Prevent the form from submitting
    const badHabitName = badHabitInput.value.trim();
    if (badHabitName !== '') {
      const newBadHabitElement = document.createElement('a');
      newBadHabitElement.setAttribute('data-bad_habit-name', badHabitName);
      newBadHabitElement.setAttribute('activated', 'on');
      newBadHabitElement.innerHTML = `${badHabitName}<i class="bi bi-dash"></i>`;
      newBadHabitElement.style.setProperty("margin-right", "5px");

      const newInputField = document.createElement('input');
      newInputField.setAttribute('type', 'hidden');
      newInputField.setAttribute('name', 'bad_habits');
      newInputField.setAttribute('value', badHabitName);

      selectedBadHabitsDiv.appendChild(newBadHabitElement);
      selectedBadHabitsDiv.appendChild(newInputField);

      badHabitInput.value = '';
    }
  }
});