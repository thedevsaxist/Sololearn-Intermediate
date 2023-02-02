# Repositories (Repo's)

- A repo is a container for a project you want to track with Git

- Can have many different repo's for many different projects on you computer

- ike a project folder which Git tracks the content of for us

>How to know a file that is being tracked by Git is the `.git` file. Now this file can be at the root of the directory, meaning that it is tracking any thing that is in that directory. Subsequently, it can be in a sub folder, meaning it is tracking just the subfolder and anything inside it but not anything outside it.

# Commits

Commits are like save points. This can be used to track our different stages of our project, allowing us to easily go back to different stages in our code.

## Modified ##

These are changed files that have not been committed.

## Staging ##

Add any changed files to staging that you want to commit.

## Committed ##

Any files in the staging area are added to the commit when we make one.

A branch is the place where commits are stored without altering the main code.

# Creating a Repo

`git init` is the code to initialize a repo in a folder. In this folder you can have different files and all these files wil be tracked by Git.
This code needs to be ran in the directory of te folder you want to create the repo in.

The change in color of the file is to represent that a change has been made to the file that is being tracked by Git. `Green` means it has been modified and has not been committed.

A repository can be created in a new folder and a file be added to it or a folder with an already existing file, and from that point on, track al changes made to hte file(s).

# Staging

We can't commit a file unless it has been staged. The command `git status` shows us the files that have been modified or staged. The red color of the file name when we run `git status` signifies that the files has been modified but has ot been added to the staging.

```git
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file.html
        main.py

nothing added to commit but untracked files present (use "git add" to track)
```

We can add a file to be committed by running `git add` followed by the file name. If we do this and we run `git status` once again, we will find out that our file has been staged and is now a green color, but it will display any file that is yet to be staged, still in red.

```git
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git add main.py
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   main.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file.html

```

We can also unstage a file we accidentally staged by running `git rm -- cached <filename>`, and if we run `git status` again, we will find out that our file has been unstaged.

```git
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git rm --cached main.py
rm 'main.py'
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file.html
        main.py

nothing added to commit but untracked files present (use "git add" to track)
```

We can use `git add .` to stage multiple files at once.

```git
PS C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git add .
PS C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   file.html
        new file:   main.py

```

Staging is mainly an added security feature which prevents us from messing up our code. It also allows us to split our work into different commits for different changes.

# Making Commits

We can commit our code by simply running `git commit -m` followed by a descriptive message of what you are committing encapsulated in double quotes.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git commit -m "I added a main.py file and an index.html file to experiment with commits"
[master (root-commit) a9c62ae] I added a main.py file and an index.html file to experiment with commits
 2 files changed, 15 insertions(+)
 create mode 100644 file.html
 create mode 100644 main.py
```

>Now when we make a commit,  we receive a message back in square brackets consisting of, the branch in which our commit was made into followed by the id of our commit, the message of the commit, the number of files committed, the number of lines of code committed, and finally the id of the files in the commit.

***Note***: `Green` means there is a new uncommitted file, while, `Orange/Blue` means a committed file has been modified.

When a committed file is edited, Git sees it as a line was deleted and a new line was added. Also note that every commit has a different id.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git commit -m "I add a new main.dart file and modified my main.py file"
[master ae81cea] I add a new main.dart file and modified my main.py file
 2 files changed, 7 insertions(+), 3 deletions(-)
 create mode 100644 main.dart
```

We can check our commit history by running `git log`. This displays the commit id, followed by the person/author who made the commit, date of commit and the commit message.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git log
commit 292e75670bc94fe0a10aaafe1c94b257a8cb3920 (HEAD -> master)
Author: Omoobaba <chidiebubeiroezindu@gmail.com>
Date:   Tue Jan 31 23:09:30 2023 +0100

    I deleted my index.html file because I no longer had use for it and i renamed my main.dart file to test.dart so as to avaoid confusion with the main.py file

commit ae81ceaa7d702d9be4c46a23800c86366c90ab82
Author: Omoobaba <chidiebubeiroezindu@gmail.com>
Date:   Tue Jan 31 23:01:28 2023 +0100

    I add a new main.dart file and modified my main.py file

commit a9c62aec34c6bbd5b01a32be26b14dfb6d482ae3
Author: Omoobaba <chidiebubeiroezindu@gmail.com>
Date:   Tue Jan 31 22:47:18 2023 +0100

    I added a main.py file and an index.html file to experiment with commits

commit a9c62aec34c6bbd5b01a32be26b14dfb6d482ae3
Author: Omoobaba <chidiebubeiroezindu@gmail.com>
Date:   Tue Jan 31 22:47:18 2023 +0100

    I added a main.py file and an index.html file to experiment with commits
```

We can have a reduced version of this by running `git log --oneline`. This instead returns just the commit id and the commit message.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git log --oneline
292e756 (HEAD -> master) I deleted my index.html file because I no longer had use for it and i renamed my main.dart file to test.dart so as to avaoid confusion with the main.py file
ae81cea I add a new main.dart file and modified my main.py file
a9c62ae I added a main.py file and an index.html file to experiment with commits
```

# Undoing Stuff

We have three different types of commit reversals:

- Checkout Commit (`Green` signifying that this is not dangerous to your code)

- Revert Commit (`Orange` signifying that this can have potential consequences but noting lethal)

- Reset Commit (`Red` signifying utter, lethal danger)

## Checkout Commit

This is a read only mode of reversal. It allows you to see what your code base was like at a point of a particular commit, it doesn't allow you to modify your code.

This is done my running `git checkout` followed by the id of the commit you want to go back to.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git checkout ae81cea
Updating files: 100% (4/4), done.
Note: switching to 'ae81cea'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at ae81cea I add a new main.dart file and modified my main.py file
```

>You can leave the commit and return back to the master branch by running `git checkout master` or `git checkout` and any branch you want to return back to.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git checkout master
Previous HEAD position was ae81cea I add a new main.dart file and modified my main.py file
Switched to branch 'master'
```

## Revert Commit

This allows change to a commit. It allows you to nullify the effects of a commit, almost like the commit was never made.

This can be accessed by running `git revert` followed by the commit you'll like to revert.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git revert 8b6377d
```

When you run this, you'll be met by a prompt asking you to add a commit message since you'll be trying to delete a commit.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git revert 8b6377d
Revert "I modified the basic.js file to output the company name"

This reverts commit 8b6377d170e3739f04d6c63fb320a317e954bb22.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
# Changes to be committed:
#       modified:   basic.js
```

Don't fear cause you can easily skip this by pressing `shift` + `;` or rather `:`, followed by `wq`.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git revert 8b6377d
[master a350bf9] Revert "I modified the basic.js file to output the company name"
 1 file changed, 1 insertion(+), 2 deletions(-)
```

Now if you run `git log`, you'll still see the old commit but you'll also find a new commit which reverts/nullifies the old commit.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git log --oneline
a350bf9 (HEAD -> master) Revert "I modified the basic.js file to output the company name"
8b6377d I modified the basic.js file to output the company name
793d129 created a basic.js file and added a function to the test.dart file
292e756 I deleted my index.html file because I no longer had use for it and i renamed my main.dart file to test.dart so as to avaoid confusion with the main.py file
ae81cea I add a new main.dart file and modified my main.py file
a9c62ae I added a main.py file and an index.html file to experiment with commits
```

## Reset Commit

This allows you to reset your commit history to a particular point. It deletes all commits made and resets it back to the specified commit. This has the potential to ruin your entire code base so be careful when using it.

You can do this by running `git reset` followed by the id of the commit you would like to reset to. Now when you run this command, the changes you made in the other commit will remain visible, but they will no longer be in you commit history when you run `git log`. This allows us to make edits and commit all the changes as just one commit.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git reset ae81cea
Unstaged changes after reset:
D       file.html
D       main.dart
```

Now we can totally erase these commits by running `git reset <commit id> --hard`.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git reset ae81cea --hard
Updating files: 100% (2/2), done.
HEAD is now at ae81cea I add a new main.dart file and modified my main.py file
```

>Now there is no way of getting back or old commits.

# Branches

Normally the master branch represents the stable version of your code. Branching allows you to modify copies of your code without actually affecting your main code base. You can later merge this branch with your main branch.

>A branch is like an isolated version of your code.

## Creating a branch

You can create a branch by running `git branch <branch name>`.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git branch feature-1
```

Now you can view all the branches under the master branch by running `git branch -a`. The branch with an asterisk prefixing it is the branch you are currently on.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git branch -a
  feature-1
* master
```

Now you can switch branches by running a `git checkout` command followed by the branch name you want to move into.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git checkout feature-1
Switched to branch 'feature-1'
```

Running the `git branch -a` command, you'll find out that the position of the asterisk has changed. This means that our branch change worked.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git branch -a
* feature-1
  master
```

> Try not to confuse this with checkout commit. Checkout commit takes the commit id after the `git checkout` command, while, a branch change takes the name of the branch after the `git checkout` command.

## Deleting a Branch

You can delete a branch by simply running `git branch -d` followed by the branch name. This type of branch delete will only work if the branch has been merged to the main branch.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git branch -d feature-1
error: The branch 'feature-1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D feature-1'.
```

To delete an unmerged branch, we run `git branch -D` followed by the branch name.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git branch -D feature-1
Deleted branch feature-1 (was a668d31).
```

To quickly create a branch an checkout into it, we run `git checkout -b` followed by the branch name.

# Merging Branches

To merge a branch, we first have to be on the branch that we want to merge into. Then to merge a branch we run `git merge` followed by the name of the branch you want to merge.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git merge feature-a
Updating 3b1ace7..271c6d3
Fast-forward
 basic.js     |  1 -
 feature-a.js |  1 +
 file.html    | 11 -----------
 3 files changed, 1 insertion(+), 12 deletions(-)
 delete mode 100644 basic.js
 create mode 100644 feature-a.js
 delete mode 100644 file.html
```

## Conflict

A conflict is an error that occurs when the same file is edited in different branch(s) and merged to the master branch.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git merge feature-c
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.
```

Don't worry all you need to do is edit the file that has the conflict, then stage the file for a commit and finally, commit the file. But when you do this an error message pops up. All you need to do is `: wq`.

```
Merge branch 'feature-c'

# Conflicts:
#       main.py
#
# It looks like you may be committing a merge.
# If this is not correct, please run
#       git update-ref -d MERGE_HEAD
# and try again.


# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
# All conflicts fixed but you are still merging.
#
# Changes to be committed:
#       modified:   main.py
```

Then the conflict will be resolved.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git add .
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git commit
[master 8b58876] Merge branch 'feature-c'
```

# Intro to GitHub

- GitHib is a service that lets us set up hosted repositories (remote repo's)

- Central online repository which multiple team-members could access.

## Pushing to GitHub

We can do this by running `git push <where you want to push it to (which is the remote repo link)> <and the branch you want to push>`

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git push https://github.com/Omoobaba/git_two.git master
Enumerating objects: 24, done.
Counting objects: 100% (24/24), done.
Delta compression using up to 4 threads
Compressing objects: 100% (21/21), done.
Writing objects: 100% (24/24), 2.68 KiB | 26.00 KiB/s, done.
Total 24 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), done.
To https://github.com/Omoobaba/git_two.git
 * [new branch]      master -> master
```

When ever you make an edit to this repo and you want to push it to a remote repo, you stage and commit the same way as usual. Now rather than writing the `Url` every time we want to push, we can instead assign an alias to the remote repo.
This can be done by running `git remote add <the alias you want to use> <the remote repo Url>`

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git remote add origin https://github.com/Omoobaba/git_two.git
```

Now when we want to push we can do so using the alias rather than the Url.

```
C:\Users\User\Desktop\Chidiebube\githublearn\git_two> git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 327 bytes | 163.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Omoobaba/git_two.git
   8b58876..e6a8c9b  master -> master
```

# Cloning a Repository from GitHub

We first have to create a remote repo and copy the `url`. Then in our terminal we can run `git clone <url>`.

```
C:\Users\User\Desktop\Chidiebube\githublearn> git clone https://github.com/Omoobaba/portfolio-map.git
Cloning into 'portfolio-map'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```

> ***Note***: We don't need to specify an alias for a cloned repo cause this has already been done for us. And you can check this out by running `git remote -v`

```
C:\Users\User\Desktop\Chidiebube\githublearn\portfolio-map> git remote -v
origin  https://github.com/Omoobaba/portfolio-map.git (fetch)
origin  https://github.com/Omoobaba/portfolio-map.git (push)
```

## Collaborating on GitHub

To keep up to date with changes made to the repo, we can pull from the repo. We do this by running `git pull <alias> <branch name>`

```
C:\Users\User\Desktop\Chidiebube\githublearn\portfolio-map> git pull origin main
From https://github.com/Omoobaba/portfolio-map
 * branch            main       -> FETCH_HEAD
Already up to date.
```

> This shows that we are up to date on all the changes. But if any change was made, it will be displayed in the terminal.

```
C:\Users\User\Desktop\Chidiebube\githublearn\portfolio-map> git pull origin main       
From https://github.com/Omoobaba/portfolio-map
 * branch            main       -> FETCH_HEAD
Updating 8c3c5e9..12edb43
Fast-forward
 main.py | 16 +++++++++-------
 1 file changed, 9 insertions(+), 7 deletions(-)
 ```

 > This is what it looks like when an edit was made

When you've created a new branch and made some edits to the code base, you **do not** just merge your branch to the main branch because that might bring up some conflict, or maybe your code might not be acceptable. Instead, you would want to push your branch instead to the repo so that it can be reviewed by your other teammates or manager and then they can merge it to the main branch if they like.

```
C:\Users\User\Desktop\Chidiebube\githublearn\portfolio-map> git push origin main-python
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 471 bytes | 117.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'main-python' on GitHub by visiting:
remote:      https://github.com/Omoobaba/portfolio-map/pull/new/main-python
remote:
To https://github.com/Omoobaba/portfolio-map.git
 * [new branch]      main-python -> main-python
```

# Forking (& Contributing)

- Forking means copying a repo from another account to your own.

- Contributing is simply working on another person's project that was made public. This is known as *Contributing to open source*.

You basically just for the repo into your account and clone to your machine.

> Before you start contributing to an open source project always check for any guidelines for contributing.
