# interview-materials

Welcome and thank you for your interest in TRI! We have prepared a basic full stack development test for you to complete. In this directory you will find photos and 3D models of cars. We have also included a simple Flask server that connects to a MySQL database that includes the name, photo file name, and model file name of each item in a `cars` table. The server as implemented now only retrives all data from that table and returns the list to the browser. The server is running live at an address that will be provided to you.

Your goal is to build a simple fullstack web UI that accomplishes some basic tasks:
- Retrieves data from the DB.
- Allows users to page through each car in a slider, carosel, or other type of view. Your UI should show at least the photo and name of each car.
- Logs user interactions (e.g., car views) to a new `log` table that you will create on the backend. Please feel free to use the basic mysql command-line to do this. E.g.:
    - `% mysql -u root`
    - `% mysql> use test;` (to select the `test` database)

Note that while we have provided you a basic Flask application, you can actually build with whatever stack you want! The VM that your hiring contact provided you is yours to configure (don't worry about containerization: we've archived the base image of this server). Please feel free to rewrite the server in your preferred framework. The same goes with the web UI: Choose any framework you like (or code in vanilla HTML/JS). Please also feel free to define the `log` table schema however you would like.

If you've done that and want to extend the app further, here are some possibilities. We will only evaluate at most one of these--please don't spend time doing any more than that!

- Extend the app to upload a new car name, photo, and model. Note this will require adding both frontend and backend code. We've left one car out of the database on the server (models/SUV.png and photos/SUV.glb, which is a "2020 BMW X4") for your testing.
- Implement a search feature (either completely on the client or using a client/server approach)
- Use a third-party library to load the 3D model and make it visually appealing (hint: we recommend using Google's model-viewer library for this).