# advanced_features_and_security/README.md
Permissions and Groups Setup
===========================

This app uses custom permissions and groups to control access to Post instances.

**Permissions**

* `can_view`: Can view post
* `can_create`: Can create post
* `can_edit`: Can edit post
* `can_delete`: Can delete post

**Groups**

* `Editors`: Can edit and create posts
* `Viewers`: Can view posts
* `Admins`: All permissions

**Views**

* `post_edit_view`: Requires `can_edit` permission
* `post_create_view`: Requires `can_create` permission