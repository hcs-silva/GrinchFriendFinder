//Check if the input field is filled
function submitForm() {
  const input = document.getElementById("nameInput").value;
  if (input.trim() !== "") {
      generateRandom();
  } else {
      alert("Please fill in the name input.");
  }
}
// Initialize the array with names
const names = ["nuno", "ines", "magda", "rosa", "hernani", "bacalhau", "bacalhauzinho", "sonia"];

// Shuffle the array to get a random order
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Call the shuffle function to randomize the order of names
shuffleArray(names);

// Function to generate a random name and update the result
function generateRandom() {
    const input = document.getElementById("nameInput").value;
    const resultElement = document.getElementById("result");

    // Check if there are names left in the shuffled array
    if (names.length > 0) {
        // Get the first name from the shuffled array
        const randomName = names.pop();

        // Check if the random name is not equal to the input
        if (randomName !== input) {
            resultElement.innerHTML = randomName.toUpperCase();

            setTimeout(() => {
              resultElement.innerHTML = "";
          }, 3000);
        } else {
            // If the random name is equal to the input, try again
            generateRandom();
        }
    } else {
        // If all names have been displayed, show a message
        resultElement.innerHTML = "All names displayed. Please click again.";
    }
}
