Purpose:
A mini Twitter clone using Django that allows users to post short messages ("tweets") with optional images.

User Authentication:
User registration and login system using Django's built-in auth.
Users must log in to create, edit, or delete tweets.

Tweet Functionality:
Tweets include a text field (max 200 characters).
Optional photo upload for each tweet.
Tweets are linked to the user who created them.

Timestamps:
Each tweet stores the date and time of creation and last update.

Media Handling:
Uploaded images are stored in a media/ directory.
Proper MEDIA_URL and MEDIA_ROOT settings are configured.

Admin Panel:
Admin can manage users and tweets through Django admin interface.

URL Routing:
Routes for listing tweets, creating, editing, deleting, logging in/out, and registering.
Clean and RESTful URL patterns.

Forms:
Custom ModelForm for tweets.
Extended UserCreationForm with an email field.

Templates:
HTML templates used for displaying tweets and forms.
Template directories properly set up in settings.

Security:
CSRF protection enabled.
Only the tweet’s owner can edit or delete it.
