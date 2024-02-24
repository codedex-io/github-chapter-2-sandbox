# Testing Git and GitHub in Codedex

Knowing how to use Git and GitHub

|Access Type|Description|
|---|---|
|Read|Users can view the repository and clone it.|
|Write|Users can read the repository and make changes, create branches, and push modifications.|
|Admin (Admin rights)|Users have full control over the repository, including settings, access permissions, and deletion.|
|Maintainer (Org)|In organizations, users with similar privileges to Admin but specific to a particular repository.|
|Collaborator|Users have read and write access to a repository.|

## Git Commands

- `git add example.txt` will add the single file to the staging area. If you only want one of your working files to show up on GitHub rather than the rest of your project, consider specifying a specific file.
- `git add .` will add _all_ the changed files to the staging area. This means that any new file added or changed to the working directory will be included.
- `git add *.html` will only stage files with a specified extension. In this example, this command will only add **.html** files.
- `git reset filename` unstages a specific file if you did not mean to stage it.
- `git reset` unstages all your files, returning back to the previous state of your working directory.