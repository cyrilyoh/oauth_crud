# Django CRUD with GitHub's OAuth
#### Candiate Name : Cyril Yohannan

## Introduction

This project aims to  build a CRUD application in a Django, that allows a user to login using the Oauth protocol, with github as the provider.

## Key Features

- **OAuth Login:**
  - A github user can login to the system.

- **Profile update:**
  - Logged-in user can view/update/delete their profile.

## Dependencies

- Django==4.2.9
- social-auth-app-django==5.4.0

## How to use locally

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
2. **Install reuirements.txt**
    ```bash
   pip install -r requirements.txt
3. **Run the app**
    ```bash
   python manage.py runserver

## Superuser credentials

- Username: cyril
- Password: cyril

## Application Screenshots

- **Login:**
    - Clicking the login button will lead to the GitHub login page. After successfully logging in with GitHub credentials, the user's profile will be presented.
    ![Login](https://github.com/cyrilyoh/oauth_crud/blob/main/screenshots/1.png)

- **Home (View/Delete profile, Logout):**
    - Here, the profile of the currently logged-in user is presented, initially appearing empty as the profile has not been created. Users can choose to update or delete the profile, and a logout button is provided.
    ![Login](https://github.com/cyrilyoh/oauth_crud/blob/main/screenshots/2.png)

- **Update profile:**
    - The current details of the user's profile are presented within a form, allowing the user to make updates. Additionally, a cancel button is provided for navigation back.
    ![Login](https://github.com/cyrilyoh/oauth_crud/blob/main/screenshots/3.png)