fetch("https://api.themotivate365.com/stoic-quote")
  .then(response => response.json())
  .then(frames => {
    const fps = 25; // frames per second
    const frameInterval = 1000 / fps; // interval between frames in milliseconds
    let currentFrameIndex = 0;

    const asciiArtElement = document.getElementById("ascii-art");

    const updateAsciiArt = () => {
      asciiArtElement.textContent = frames[currentFrameIndex].frame;
      currentFrameIndex = (currentFrameIndex + 1) % frames.length;
    };

    setInterval(updateAsciiArt, frameInterval);
  })
  .catch(error => console.error(error));
