# MinimumWebService

We will gather here samples of the simplest web services we can create, 
to serve as examples for students who have not done back-end web development
before.  I will start with a Python Flask example.  I invite others to fill
in examples with different languages, frameworks, and databases, 
all providing an equivalent nanoTwitter service. 

Structure should be MinimumWebService/language/framework .  If possible support 
multiple databases within a single framework directory, but if necessary 
create a language/framework/database directory. 

For example, I will begin by creating MinimumWebService/Python3/Flask, initially 
with one database / storage service; I hope to extend it to dynamically support 
MongoDB, SQLite, and Redis (or to persuade someone who knows SQLite and Redis better
than me to add that support). 

(I am realizing now that git is quite inflexible in managing hierarchy; it is not possible to 
clone just one subfolder of this set of examples, which among other things makes deployment
to a cloud service difficult or impossible.  That's a step backward from subversion. 
Grumble grumble, get off my lawn.  We may break this out into a separate 
repository per framework, although I would prefer to keep them together.) 
