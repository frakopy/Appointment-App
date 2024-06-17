// Variables for work with appointments.html
const dateForm = document.getElementById("date-form");
const inputDate = document.getElementById("newDate");
const inputTime = document.getElementById("newTime");
const urlAvailability = document.getElementById("url-availability");
const btnElements = document.getElementsByClassName("btn-reschedule");
const btnList = Array.from(btnElements);


btnList.forEach((element) => {
  element.addEventListener("click", (e) => {
    const appointmentId = e.target.dataset.appointmentid;
    const barberId = e.target.dataset.barberid;
    const eventId = e.target.dataset.eventid;
    inputDate.setAttribute("data-barberId", barberId);
    dateForm.action = dateForm.action + `?id=${appointmentId}&event-id=${eventId}`;
  });
});


// ------------------Get availability from backend----------------------------------------


// Add list of available hours to time field
const addHours = (hoursList) => {
  inputTime.innerHTML = "";
  hoursList.forEach((hour) => {
    const newHour = document.createElement("option");
    newHour.value = hour;
    newHour.textContent = hour;
    inputTime.appendChild(newHour);
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
  const barberId = inputDate.dataset.barberid;
  const selectedDate = inputDate.value;
  const url = urlAvailability.dataset.url;
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
    const request = await fetch(url, fetchSettings);
    const result = await request.json();
    return result;
  } catch (error) {
    return error;
  }
};

// Send POST request to the backend in order to obtain a list of available hours
inputDate.addEventListener("change", () => {
  getHours().then((response) => {
    if (response.result === "ok") {
      const hoursList = response.hours;
      addHours(hoursList); //Call function to add available hours
      inputTime.removeAttribute("disabled");
    }
  });
});


// Display calendar on click 
inputDate.addEventListener("click", (e) => {
  inputDate.showPicker();
});