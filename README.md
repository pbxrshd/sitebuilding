# Site building related
=====================

reference links
---------------

* (https://chadthompson.me/2013/05/static-web-hosting-with-amazon-s3/)
* (http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)
* (http://www.bloggeryard.com/2013/11/create-blogger-template-from-scratch.html)
* (http://www.blogxpertise.com/)
* (https://developers.google.com/blogger/docs/3.0/getting_started#background-operations)
* [good site](http://alignedleft.com/resources/cheap-web-hosting)
* (http://katsenblog.com/post/85144002449/how-anyone-in-the-world-can-create-cheap-static-sites)
* [markdown cheat sheet](http://assemble.io/docs/Cheatsheet-Markdown.html)
* [dns](https://dnsimple.com/)


sample sites
------------
* (http://www.rebekahbrooks.com/) blogger site
* (http://www.suttermeats.com/) blogger site
* (http://www.flashmint.com/)

dev
---
* $python -m SimpleHTTPServer 8081

site layout 
-----------
* header
   * title
   * links
* about blurb
* upcoming | recent event
* picture slide show
* quote
* blog list
* footer

Design notes:
-------------
all content is under content
pages are under content/
posts are under content/post

move deleted to content/deleted 


admin functions:
 - get returns admin page
 - given a page name, 
   - retrieve the page
   - parse out h1, h2 into text boxes, p into textarea
   - within p, support li, hrefs, img, bold, italic 
   - add h2, p
   - convert to html
   - upload to save


tafakur.ttf was the font used to generate the logo



    
to alias and run python from command line, add this entry in .bashrc

httpserver() { python2.7 ~/pathTo/admin.py ${1:-8000} ;}

now can invoke $ httpserver
or $ httpserver 60660 # to override default port 8000



## git related
 git status
 git ad --all
 git commit -m "comment"
 git push origin
 
