# Token authentication: 

## clients authenticate by providing a unique token in the request header.
# Session authentication: 
## clients authenticate using django's built-in session-based authentication

# OAuth Authentication: 
## clients authenticate using the OAuth 2.0 protocol, which allows third party applications to access user data without requiring their credentials

## You can configure authentication globally in your settings.py or at the view or viewset level using authentication_classes

# Permission Policies in DRF
## (a) AllowAny
### Allow access to anyone regardless of authentication status
## (b) IsAuthenticated
### Allow access only to authenticated users
## (c) IsAdminUser
### Allow access only to users with the is_staff flag set to True
## (d) IsOwner
### Allow access only to the owner of the resource


# MyModelListView 

## requires token based authentication and the IsAuthenticated permission, which means only authenticated users can view the list of models

# MyModelCreateView
## requires token-based authentication and the IsAdminUser permission, which means only admin users can create new model instances