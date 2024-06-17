const barber = document.getElementById("id_barber");
const date = document.getElementById("id_date");
const time = document.getElementById("id_time");
const inputUrl = document.getElementById("url");
const hoursUrl = inputUrl.dataset.url;


barber.addEventListener("change", () => {
  date.removeAttribute("disabled");
  if (date.value) {
    getHours().then((response) => {
      if (response.result === "ok") {
        const hoursList = response.hours;
        addHours(hoursList); //Call function to add available hours
        time.removeAttribute("disabled");
      }
    });
  }
});

// Add list of available hours to time field
const addHours = (hoursList) => {
  time.innerHTML = "";
  hoursList.forEach((hour) => {
    const newHour = document.createElement("option");
    newHour.value = hour;
    newHour.textContent = hour;
    time.appendChild(newHour);
  });
};

// Get csrftoken, the code of this function is provided by django documentation
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Function to send the form to the backend
const getHours = async () => {
  // Setting data to be sent to the backend
  const barberId = barber.value;
  const selectedDate = date.value;
  const dataTosend = { date: selectedDate, barberId: barberId };

  //Get the CSRF token using the function code provided by django documentation
  const csrftoken = getCookie("csrftoken");

  const fetchSettings = {
    method: "POST",
    credentials: "same-origin",
    body: JSON.stringify(dataTosend),
    headers: { "X-CSRFToken": csrftoken },
  };

  try {
    const request = await fetch(hoursUrl, fetchSettings);
    const result = await request.json();
    return result;
  } catch (error) {
    return error;
  }
};

// Send POST request to the backend in order to obtain a list of available hours
date.addEventListener("change", () => {
  getHours().then((response) => {
    if (response.result === "ok") {
      const hoursList = response.hours;
      addHours(hoursList); //Call function to add available hours
      time.removeAttribute("disabled");
    }
  });
});

// Display calendar on click 
date.addEventListener("click", (e) => {
  date.showPicker()
});

