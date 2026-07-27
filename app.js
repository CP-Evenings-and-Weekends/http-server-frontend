const characterButton = document.querySelector(
  "#character-button"
);

const characterName = document.querySelector(
  "#character-name"
);

const movieTitle = document.querySelector(
  "#movie-title"
);

characterButton.addEventListener("click", () => {
  fetch("http://localhost:9292/horror-character")
    .then((response) => response.json())
    .then((data) => {
      characterName.textContent = data.character;
      movieTitle.textContent = `${data.movie}`;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});