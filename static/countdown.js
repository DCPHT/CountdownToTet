function convert(time){
  if(time < 10){
    return '0'+ time
  }
  return time;
}

// Get data from python
var tet_date;
fetch("/security")
  .then(function (response) {
    return response.json(); // But parse it as JSON this time
  })
  .then(function (json) {
    tet_date = json.date;
    var countDownDate = new Date(tet_date).getTime();
    var x = setInterval(function () {
      // Get today's date and time
      var now = new Date().getTime();

      // Find the distance between now and the count down date
      var distance = countDownDate - now;

      // Time calculations for days, hours, minutes and seconds
      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor(
        (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      // Display the result
      document.getElementById("days").innerText = convert(days),
      document.getElementById("hours").innerText = convert(hours),
      document.getElementById("minutes").innerText = convert(minutes),
      document.getElementById("seconds").innerText = convert(seconds);

      document.getElementById("countdown").hidden = false;
      // If the count down is finished, write some text
      if (distance <= 0) {
        clearInterval(x);
        document.getElementById("lunar").innerHTML = "CHÚC MỪNG NĂM MỚI";
        document.getElementById("lunar").hidden = false;
        document.getElementById("countdown").hidden = true;
        document.getElementById("headline").hidden = true;
        document.getElementById("endline").hidden = false;
        document.getElementById("canvas-container").hidden = false;
        document.getElementById("music").play();
      }
    }, 1000);
  });
// // POST data to python
// fetch("/security", {
//   // Declare what type of data we're sending
//   headers: {
//     "Content-Type": "application/json",
//   },

//   // Specify the method
//   method: "POST",

//   // A JSON payload
//   body: JSON.stringify({
//     greeting: "Hello from the browser!",
//   }),
// })
//   .then(function (response) {
//     // At this point, Flask has printed our JSON
//     return response.text();
//   })
//   .then(function (text) {
//     console.log("POST response: ");

//     // Should be 'OK' if everything was successful
//     console.log(text);
//   });
// Set the date we're counting down to

// Update the count down every 1 second
