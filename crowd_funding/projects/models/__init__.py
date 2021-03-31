from .images import Images
from .projects import Projects
from .raiting import Raiting
from .tags import Tags

""" 
# to create a report for a project check how we do it in the comment reported model

****************************************************

# to create projct tag you should have an exist project saved in the data base then,

Tags.objects.create(tag_name='the tage name you want', project='the projectInstaceYouHave')\

**********************************************************************
# to create projct image you should have an exist project saved in the data base then,

Raiting.objects.create(one_star='number', two_stre, .....,  project='the projectInstaceYouHave')


*******************************************************
!!! if you have an object you can simply use this metho

myProjectObject.tags_set.create(the paramater needed)
myProjectObject.images_set.create(the paramater needed)
myProjectObject.raiting_set.create(the paramater needed)

*************************************************
!!! to get all the raing for some porjct jsut like craete but .all()
myProjectObject.raiting_set.all()

Got it!

"""
