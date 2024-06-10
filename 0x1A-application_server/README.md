# Application server

This project focused on deploying our AirBnB clone application. I configured Nginx on web servers provided by Holberton School to serve a WSGI Flask app running through Gunicorn. Additionally, I set up an Upstart script to ensure the application restarts on server reboots.

 Tasks :page_with_curl:

 0. Set up development with Python
   In this task, I configured the file `web_flask/0-hello_route.py` from my
  AirBnB_clone_v2(https://github.com/bdbaraban/AirBnB_clone_v2) repository to serve content
  at the `/airbnb-onepage/` route on port `5000`.

 1. Set up production with Gunicorn
   This task involved creating a production environment by installing and configuring
  Gunicorn to serve the same file from task 0.

 2. Serve a page with Nginx
   2-app_server-nginx_config(./2-app_server-nginx_config): This Nginx configuration file
  proxies requests from the `/airbnb-onepage/` route to the Gunicorn app running on
  port `5000`.

 3. Add a route with query parameters
   3-app_server-nginx_config(./3-app_server-nginx_config): This Nginx configuration file
  proxies requests from the `/airbnb-dynamic/number_odd_or_even/<int:num>` route to the
  Gunicorn app running on port `5000`.

4. Configure the API
In this task, I set up the API from my AirBnB_clone_v3 to run on Gunicorn.
4-app_server-nginx_config: Nginx configuration file that proxies requests to the AirBnB API running on Gunicorn.
5. Serve the complete AirBnB clone
I configured the full AirBnB application from AirBnB_clone_v4 to run on Gunicorn and be served via Nginx.
5-app_server-nginx_config: Nginx configuration file to serve static assets from web_dynamic/static/ and the Gunicorn AirBnB app.
6. Deployment
gunicorn.conf: Configuration file for an Upstart script that starts a Gunicorn process on port 5003 to serve the content from task 5.
The Gunicorn process is set to spawn three worker processes and log errors to /tmp/airbnb-error.log and access logs to /tmp/airbnb-access.log.
7. Ensure no service interruption
4-reload_gunicorn_no_downtime: Bash script to gracefully reload Gunicorn without downtime.



