# interview-materials

Welcome and thank you for your interest in TRI! We have prepared a basic full stack development test for you to complete. In this directory you will find photos and 3D models of cars. We have also included a simple Flask server that connects to a MySQL database that includes the name, photo file name, and model file name of each item in a `cars` table. There is also a `log` table. The server as implemented now only retrives all data from both tables and returns them to the browser. The server is running live at an address that will be provided to you.

Your goal is to build a simple fullstack web UI that accomplishes some basic tasks:
- Retrieves data from the DB.
- Allows users to page through each model. Your UI should show at least the model photo and name.
- Logs user interactions to the `log` table. 

Note that while we have provided you a basic Flask application, you can actually build with whatever you want! The VM that your hiring contact with you is completely yours (don't worry: we've archived the base image). Please feel free to rewrite the server in your preferred framework. The same goes with the web UI: Choose any framework you like (or code in vanilla HTML/JS). For the `log` data field we recommend JSON (with at least one field being the datetime to milisecond precision).

If you've done that and want to extend the app further, here are some possibilities. We will only evaluate at most one of these--please don't spend time doing any more than that!

- Extend the app to upload a new car name, photo, and model. Note this will require adding both frontend and backend code. We've left one car out of the database on the server(SUV.png/SUV.glb, which is a "2020 BMW X4") for your testing.
- Implement a search feature (either completely on the client or using a client/server approach)
- Use a third-party library to load the 3D model and make it visually appealing (hint: we recommend using Google's model-viewer library for this).