const url = "https://api.jsonbin.io/v3/b/64380540c0e7653a05a38753";

      fetch(url, {
        headers: {
          "X-Master-Key":
            "$2b$10$XFW/PG7eCgAbENSHVYHSl.cOEXwN7gOnYG/ZNY1PFa9ltbXvASL7y",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          const frames = data.record;
          let currentFrame = 0;
          const renderFrame = () => {
            const frame = frames[currentFrame].frame;
            document.getElementById("animation").textContent = frame;
            currentFrame = (currentFrame + 1) % frames.length;
          };
          setInterval(renderFrame, 100);
        })
        .catch((error) => console.error(error));