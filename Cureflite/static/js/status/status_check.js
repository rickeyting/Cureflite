document.addEventListener('DOMContentLoaded', function() {
  const popupOverlays = document.querySelectorAll('.popup-overlay');
  const closeIcons = document.querySelectorAll('.close-icon');
  
  popupOverlays.forEach((popupOverlay) => {
    const bodyGroupName = popupOverlay.getAttribute('body-group-name');
    const clickableElement = document.querySelector(`[data-position="${bodyGroupName}"]`);
    clickableElement.addEventListener('click', () => {
      popupOverlay.style.display = 'flex';
    });
  });

  closeIcons.forEach((closeIcon) => {
    const popupOverlay = closeIcon.parentElement.parentElement.parentElement;

    closeIcon.addEventListener('click', () => {
      popupOverlay.style.display = 'none';
    });
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const checkboxes = document.querySelectorAll('.popup-content input[name="symptom_groups"][type="checkbox"]');
  const symptomsGroupInput = document.getElementById('symptoms-group-input');

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', () => {
      const symptomName = checkbox.nextElementSibling.textContent.trim();
      const symptomItems = document.querySelectorAll(`A[data-symptom-name="${symptomName}"]`);
      const symptomInputs = document.querySelectorAll(`input[name="symptoms_group"][value="${symptomName}"]`);

      if (checkbox.checked) {
        if (symptomItems.length === 0) {
          const listItem = document.createElement('a');
          listItem.setAttribute('data-symptom-name', symptomName);
          listItem.innerHTML = `${symptomName}<i class="bi bi-dash"></i>`;
          listItem.style.setProperty("margin-right", "5px");
          listItem.addEventListener('click', () => {
            listItem.remove();
            checkboxes.forEach((checkbox) => {
              if (checkbox.value === symptomName) {
                checkbox.checked = false;
              }
            });
            inputField = document.querySelector(`input[name="symptoms_group"][value="${symptomName}"]`);
            if (inputField) {
              inputField.remove(); // Remove corresponding hidden input field
            }
          });

          const newInputField = document.createElement('input');
          newInputField.setAttribute('type', 'hidden');
          newInputField.setAttribute('name', 'symptoms_group');
          newInputField.setAttribute('value', symptomName);

          symptomsGroupInput.appendChild(listItem);
          symptomsGroupInput.appendChild(newInputField);

          checkboxes.forEach((checkbox) => {
          if (checkbox.value === symptomName) {
            checkbox.checked = true;
            }
          });
        }
      } else {
        symptomItems.forEach((item) => {
          item.remove();
        });
        symptomInputs.forEach((item) => {
          item.remove();
        });
        checkboxes.forEach((checkbox) => {
          if (checkbox.value === symptomName) {
            checkbox.checked = false;
          }
        });
      }
    });
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const checkboxes = document.querySelectorAll('.popup-content input[name="bad_habit_groups"][type="checkbox"]');
  const habitsGroupInput = document.getElementById('habits-group-input');

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', () => {
      const habitName = checkbox.nextElementSibling.textContent.trim();
      const habitItems = document.querySelectorAll(`A[data-habit-name="${habitName}"]`);
      const habitInputs = document.querySelectorAll(`input[name="habits_group"][value="${habitName}"]`);

      if (checkbox.checked) {
        if (habitItems.length === 0) {
          const listItem = document.createElement('a');
          listItem.setAttribute('data-habit-name', habitName);
          listItem.innerHTML = `${habitName}<i class="bi bi-dash"></i>`;
          listItem.style.setProperty("margin-right", "5px");
          listItem.addEventListener('click', () => {
            listItem.remove();
            checkboxes.forEach((checkbox) => {
              if (checkbox.value === habitName) {
                checkbox.checked = false;
              }
            });
            inputField = document.querySelector(`input[name="habits_group"][value="${habitName}"]`);
            if (inputField) {
              inputField.remove(); // Remove corresponding hidden input field
            }
          });

          const newInputField = document.createElement('input');
          newInputField.setAttribute('type', 'hidden');
          newInputField.setAttribute('name', 'habits_group');
          newInputField.setAttribute('value', habitName);

          habitsGroupInput.appendChild(listItem);
          habitsGroupInput.appendChild(newInputField);

          checkboxes.forEach((checkbox) => {
          if (checkbox.value === habitName) {
            checkbox.checked = true;
            }
          });
        }
      } else {
        symptomItems.forEach((item) => {
          item.remove();
        });
        symptomInputs.forEach((item) => {
          item.remove();
        });
        checkboxes.forEach((checkbox) => {
          if (checkbox.value === habitName) {
            checkbox.checked = false;
          }
        });
      }
    });
  });
});


window.addEventListener('pageshow', (event) => {
  const symptomCheckboxes = document.querySelectorAll('.popup-content input[name="symptom_groups"][type="checkbox"]');
  const bad_habitCheckboxes = document.querySelectorAll('.popup-content input[name="bad_habit_groups"][type="checkbox"]');
  const habitsGroupInput = document.getElementById('habits-group-input');
  const symptomsGroupInput = document.getElementById('symptoms-group-input');
  bad_habitCheckboxes.forEach((checkbox) => {
    if (checkbox.checked) {
        const habitName = checkbox.nextElementSibling.textContent.trim();
        inputField = document.querySelector(`input[name="habits_group"][value="${habitName}"]`);
        if (!inputField) {
        const listItem = document.createElement('a');
        listItem.setAttribute('data-habit-name', habitName);
        listItem.innerHTML = `${habitName}<i class="bi bi-dash"></i>`;
        listItem.style.setProperty("margin-right", "5px");
        listItem.addEventListener('click', () => {
        listItem.remove();
        checkboxes.forEach((checkbox) => {
          if (checkbox.value === habitName) {
            checkbox.checked = false;
          }
        });
        inputField = document.querySelector(`input[name="habits_group"][value="${habitName}"]`);
        if (inputField) {
          inputField.remove(); // Remove corresponding hidden input field
        }
        });
        const newInputField = document.createElement('input');
        newInputField.setAttribute('type', 'hidden');
        newInputField.setAttribute('name', 'habits_group');
        newInputField.setAttribute('value', habitName);
        habitsGroupInput.appendChild(listItem);
        habitsGroupInput.appendChild(newInputField);
        }
    }
  });
  symptomCheckboxes.forEach((checkbox) => {
    if (checkbox.checked) {
        const symptomName = checkbox.nextElementSibling.textContent.trim();
        inputField = document.querySelector(`input[name="symptoms_group"][value="${symptomName}"]`);
        if (!inputField) {
        const listItem = document.createElement('a');
        listItem.setAttribute('data-symptom-name', symptomName);
        listItem.innerHTML = `${symptomName}<i class="bi bi-dash"></i>`;
        listItem.style.setProperty("margin-right", "5px");
        listItem.addEventListener('click', () => {
        listItem.remove();
        checkboxes.forEach((checkbox) => {
          if (checkbox.value === symptomName) {
            checkbox.checked = false;
          }
        });
        inputField = document.querySelector(`input[name="symptoms_group"][value="${symptomName}"]`);
        if (inputField) {
          inputField.remove(); // Remove corresponding hidden input field
        }
        });
        const newInputField = document.createElement('input');
        newInputField.setAttribute('type', 'hidden');
        newInputField.setAttribute('name', 'symptoms_group');
        newInputField.setAttribute('value', symptomName);
        symptomsGroupInput.appendChild(listItem);
        symptomsGroupInput.appendChild(newInputField);
        }
    }
  });
});


// Symptom section
const symptomInput = document.getElementById('symptom-input');
const selectedSymptomsDiv = document.getElementById('symptoms-group-input');

symptomInput.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault(); // Prevent the form from submitting
    const symptomName = symptomInput.value.trim();
    inputField = document.querySelector(`input[name="symptoms_group"][value="${symptomName}"]`);
    if (symptomName !== '' && !inputField) {
      const checkboxes = document.querySelectorAll('.popup-content input[name="symptom_groups"][type="checkbox"]');
      const newSymptomElement = document.createElement('a');
      newSymptomElement.setAttribute('data-symptom-name', symptomName);
      newSymptomElement.innerHTML = `${symptomName}<i class="bi bi-dash"></i>`;
      newSymptomElement.style.setProperty("margin-right", "5px");

      newSymptomElement.addEventListener('click', () => {
        newSymptomElement.remove();
        checkboxes.forEach((checkbox) => {
          if (checkbox.value === symptomName) {
            checkbox.checked = false;
          }
        });
        inputField = document.querySelector(`input[name="symptoms_group"][value="${symptomName}"]`);
        if (inputField) {
          inputField.remove(); // Remove corresponding hidden input field
        }
        });


      const newInputField = document.createElement('input');
      newInputField.setAttribute('type', 'hidden');
      newInputField.setAttribute('name', 'symptoms_group');
      newInputField.setAttribute('value', symptomName);

      selectedSymptomsDiv.appendChild(newSymptomElement);
      selectedSymptomsDiv.appendChild(newInputField);

      symptomInput.value = '';

      checkboxes.forEach((checkbox) => {
      if (checkbox.value === symptomName) {
        checkbox.checked = true;
        }
      });
    }
  }
});

// Bad habit section
const badHabitInput = document.getElementById('bad_habit-input');
const selectedBadHabitsDiv = document.getElementById('habits-group-input');

badHabitInput.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault(); // Prevent the form from submitting
    const badHabitName = badHabitInput.value.trim();
    inputField = document.querySelector(`input[name="habits_group"][value="${badHabitName}"]`);
    if (badHabitName !== '' && !inputField) {
      const checkboxes = document.querySelectorAll('.popup-content input[name="bad_habit_groups"][type="checkbox"]');
      const newBadHabitElement = document.createElement('a');
      newBadHabitElement.setAttribute('data-bad_habit-name', badHabitName);
      newBadHabitElement.innerHTML = `${badHabitName}<i class="bi bi-dash"></i>`;
      newBadHabitElement.style.setProperty("margin-right", "5px");

      newBadHabitElement.addEventListener('click', () => {
        newBadHabitElement.remove();
        checkboxes.forEach((checkbox) => {
          if (checkbox.value === badHabitName) {
            checkbox.checked = false;
          }
        });
        inputField = document.querySelector(`input[name="habits_group"][value="${badHabitName}"]`);
        if (inputField) {
          inputField.remove(); // Remove corresponding hidden input field
        }
        });

      const newInputField = document.createElement('input');
      newInputField.setAttribute('type', 'hidden');
      newInputField.setAttribute('name', 'habits_group');
      newInputField.setAttribute('value', badHabitName);

      selectedBadHabitsDiv.appendChild(newBadHabitElement);
      selectedBadHabitsDiv.appendChild(newInputField);

      badHabitInput.value = '';

      checkboxes.forEach((checkbox) => {
      if (checkbox.value === badHabitName) {
        checkbox.checked = true;
        }
      });
    }
  }
});

