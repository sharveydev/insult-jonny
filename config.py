"""
config.py: Settings and Configurations for Our App

This file is like the settings panel of our app. Here, we keep various configuration 
settings that our app needs to run properly. Think of it as a list of rules and setup 
details for our app.

What's Inside:
- We define different 'classes' here, each with settings for different situations. 
  For example, we might have one class for when we're developing the app and another 
  for when the app is running for real users.
- Settings include things like where our database is located, secret keys for security, 
  and other technical details.

How it Connects to Other Files:
- __init__.py: When we start our app in __init__.py, we use the settings from here to 
  set up everything correctly.
- We can also use different parts of this file in other areas of our app where specific 
  configurations are needed.

When to Use This File:
- Update this file when you need to change settings for your app, like switching databases 
  or changing security keys.

"""
