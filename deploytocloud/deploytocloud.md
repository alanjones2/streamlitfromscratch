
# Publish Your Streamlit Apps in the Cloud

Share your Streamlit apps with these free tools: Streamlit Cloud, Github and VSCode

![A sample Streamlit app running on Streamlit Cloud ÔÇö screenshot and app by author](https://cdn-images-1.medium.com/max/3682/1*ALw0MOKd6xDTPjUkgrWoiQ.png)*A sample Streamlit app running on Streamlit Cloud ÔÇö screenshot and app by author*

You have created an excellent Data Science app using Streamlit and it is only natural that you want to share it with the world.

Well thatÔÇÖs fine, because Streamlit Cloud lets you publish an unlimited number of public apps for nothing. You can have an entire gallery of apps, if you want, and all the tools you need to create and publish them are free.

In this article, we are going to go through the steps you need to take to publish your first Streamlit app.

But first you need three things: a Streamlit Cloud account, a Github repository for each app and, to make life easy for yourself, an editor than plays nicely with Github (IÔÇÖll be using VSCode in this article).

There four steps to publishing a Streamlit app:

* *develop your app and test it locally*

* *create a Github repository for the app*

* *push the local app to Github*

* *create a new app in Streamlit Cloud and connect it to the repo*

There is a little setting up to do before all that will work but once done publishing and updating are simple.

### Github

WeÔÇÖll start in the middle with Github. You need to set up an account, so go to the [GitHub](https://github.com/) website and do that first. YouÔÇÖll be asked to jump through a few hoops to get started but nothing too difficult ÔÇö just follow the instructions.

There are different Github accounts but for our purposes all we need is the basic free one.

Once you have an account you can create you first repository. Either click on the green *Create repository* button or the *Start a project *button.

![Screenshot by author](https://cdn-images-1.medium.com/max/2056/1*oD68W7OviiwBweOr7W0DAQ.png)*Screenshot by author*

This will bring up a form for you to fill in:

![Screenshot by author](https://cdn-images-1.medium.com/max/2000/1*_oPLDWrI3UQa_-FFR4ct2g.png)*Screenshot by author*

Give the repo a name (where it says ÔÇÿtempÔÇÖ in the image above) and a description, and make sure that the *Public* option is selected.

You will then be asked to to specify some options. ItÔÇÖs a good idea to create a README file, itÔÇÖs where you can describe the purpose of the repo and its contents, so select that and it will be automatically created for you.

*gitignore *is a way of instructing Git to ignore particular types of files that you donÔÇÖt want to include in the repo ÔÇö forget it for now, we wonÔÇÖt be using it.

Finally, choose a license and click *Create repository*.

![Screenshot by author](https://cdn-images-1.medium.com/max/2000/1*xNuNFBJKYx1ZGHYezlXcQg.png)*Screenshot by author*

You know have a place to keep the code for your Streamlit app that can be read by anyone ÔÇö mostly importantly by Streamlit Cloud.

You now have a basic repo that can be downloaded onto your local machine. To do this we *clone* the repo. Click on the code button and copy the url ÔÇö you will use this in VSCode in a moment.

![Cloning a repository in GitHub ÔÇö image by author](https://cdn-images-1.medium.com/max/2000/0*nNiuOkV-FOVbhPg6.png)*Cloning a repository in GitHub ÔÇö image by author*

### VSCode

Now letÔÇÖs turn to the editor. If you donÔÇÖt already have VSCode then download and install it, along with the Python extension (IÔÇÖm assuming that you have Python, already).

Open VSCode, close any files or folders that you have open and select the *source control *icon. This gives you the option to open an existing Git repo or clone a new one. We are going to do the latter.

![Creating a repository in VSCode ÔÇö image by author](https://cdn-images-1.medium.com/max/2000/0*2nw7kVxkMypXOa-9.png)*Creating a repository in VSCode ÔÇö image by author*

Click on *Clone Repository* and youÔÇÖll be asked for a url ÔÇö thatÔÇÖs the one that we copied a moment ago from the GitHub webpage, so paste it in.

Hit return and youÔÇÖll be asked whether you want to open the repo ÔÇö you do, of course. It may then ask if you trust the authors of the repo ÔÇö again, you do (you trust yourself, right?).

After a second or two you should have something like this:

![A new repository in VSCode ÔÇö image by author](https://cdn-images-1.medium.com/max/2000/1*rxy2BZzKD53inAZBTxyJjA.png)*A new repository in VSCode ÔÇö image by author*

Now we are ready to create a new app.

Here IÔÇÖve created a simple Streamlit app and am about to run it from the terminal window.

![A new app ÔÇö screenshot by author](https://cdn-images-1.medium.com/max/2528/1*Yg7JWTBaCsMBZxnq3DLisA.png)*A new app ÔÇö screenshot by author*

It runs ok:

![Sample app ÔÇö screenshot by author](https://cdn-images-1.medium.com/max/2000/1*ArPRiYkwbvVqVGdQpM03NQ.png)*Sample app ÔÇö screenshot by author*

So now we are ready to upload it to our new Github repo.

Notice that, in VSCode, the source control icon now has a notification ÔÇö this is because something has changed. Open the source control icon again and and you can see that *Changes* lists *stapp1.py*.

### A quick word about Git

Git is the source control system used by Github,

Fundamentally, it tracks any changes that you make in you code ÔÇö edit a file and Git knows about it. But in order to update a project, you need to *commit* the changes. There are two parts to *commiting*, first you add the files you want to the commit ÔÇö thatÔÇÖs called staging ÔÇö and then you actually commit the changes with a short message (typically describing what changes you have made). In this way Git keeps a repository of code which contains the up-to-date files for the latest version along with a history of what changes have been made.

Once a version of your code is *commited *it can be *pushed* to a remote repository like GitHub and shared with the world (or your team).

Conversely, a version of the code can be *pulled* from the remote repository to a local machine to be worked on there and then pushed back to the remote repository when youÔÇÖve finished.

### Back to the app

We can now commit our change by typing in a commit message and hitting Ctrl+Enter.

![screenshot by author](https://cdn-images-1.medium.com/max/2000/1*vkL0dyM67nm4eQkIy8bZyg.png)*screenshot by author*

Now since we havenÔÇÖt *staged* the change, VSCode asks if you would like to automatically stage them and whether you should always do this (or never). I never bother to stage things because I always want all my changes to be in the commit ÔÇö if you want the same then choose *Yes* or *Always*. If you choose *Never*, you will have to do the staging manually.

![Automatic staging ÔÇö image by author](https://cdn-images-1.medium.com/max/2000/0*qwjOzVm6vIFiFvU3.png)*Automatic staging ÔÇö image by author*

You should now notice that the notification has gone.

Now the whole point of us doing all this is to keep our code on GitHub so having made a change we now need to push it there.

![Screenshot by author](https://cdn-images-1.medium.com/max/2000/1*E9q3Y0pn9KB-pLzr3-q48w.png)*Screenshot by author*

Just click the blue button and the changes will be pushed to your Github repo.

The first time you do this GitHub needs to know that you are authorized to push to your repo. First step:

![Screenshot by author](https://cdn-images-1.medium.com/max/2000/0*LtZ9O54ANK3P8QLy.png)*Screenshot by author*

This brings up a browser window and asks you log in to GitHub in the usual way to confirm that VSCode can use your account.

When youÔÇÖve done that the local repo will be pushed to GitHub.

Success!

We have created our app, pushed it to Github and now all we have to do is tell Streamlit Cloud about it!

### Streamlit Cloud

There are a few plans that you can sign up to. The one we want is the *Starter *plan. This is free and letÔÇÖs you publish an unlimited number of public Streamlit apps (and one private one).

So go to the [Streamlit Cloud web page](https://streamlit.io/cloud) and scroll down until you find the sign-up section. When I signed up, I had to do so with either my Google or Github account, which is fine by me, but I believe other signup options are in the pipeline. I signed up with Github and, of course, Streamlit Cloud needs to be able to access your Github repositories in order to access your apps.

Once youÔÇÖve sorted out your Streamlit Cloud account the rest is plain sailing.

![Screenshot by author](https://cdn-images-1.medium.com/max/3502/1*Yux3wILpnhxLZ1ookbUIFQ.png)*Screenshot by author*

Click on *New App *and you will be asked for the details of your app:

![screenshot by author](https://cdn-images-1.medium.com/max/2002/1*taPdyV_v-9JG7W5NjiBkVQ.png)*screenshot by author*

Type in the repository path and the name of the Streamlit app file and click *Deploy *(the Branch stays as ÔÇÿmainÔÇÖ).

Streamlit now appears to be ÔÇÿbakingÔÇÖ your app:

![Screenshot by author](https://cdn-images-1.medium.com/max/3020/1*9NL0PgzisRXY9UqBgFrcSA.png)*Screenshot by author*

The panel on the right tells you what is actually going on, while the icon on the left cycles through a variety of foodstuffs (the one above is supposed to be a potato).

After a while you get a burst of cartoon balloons to celebrate the fact that you app is ready for consumption and it duly appears on the screen.

And that is it. You can go through the with as many public apps as you like. The only real restraint is that if your app doesnÔÇÖt receive much traffic, Streamlit puts it to sleep in order not to waste resources. When asleep the app is still available but it will have to go through the ÔÇÿbakingÔÇÖ process again before it runs. Streamlit will send you a friendly email telling you when they are going to do this and suggesting that, if you want to you can simply visit your app to prevent it from dozing off.

So we have seen just how straightforward it is to publish your Streamlit app using entirely free tools. I hope it has been useful and that IÔÇÖll see your apps in the Cloud soon. Please do drop a comment below with a link if you do that. You can find some of my simple efforts [here](https://share.streamlit.io/alanjones2/ajstreamlit/main/index2.py).

---

Thanks for reading and if you would like to know when more Streamlit articles are published, subscribe to the free occasional newsletter on [Substack](https://streamlitfromscratch.substack.com/).
