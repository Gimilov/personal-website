# My personal website
My personal website as a final project for CS50 by Harvard using Python, Flask, HTML, CSS, JavaScript and Bulma.

The website will be, of course, improved continuously (adding SQL, more JavaScript etc.).

### Description:

The personal website was in my biggest need in the current time. Below I present the elements of the whole website and the reasoning behind that.

- ## app.py

The controller of the whole website. Renders given templates and set routes to them. Though yet simple and short, I will broaden it over time.

- ## layout.html

Sets the layout for all templates. I've decided to include here the typical elements of each HTML file and main part of the navbar and a little of JavaScript at the end of <body> tag. 

The navbar in layout contains the logo is stylized with the help of both Bulma CSS Framework and styles.css. It also is very responsive and has it's own option for mobile devides. 

Moreover, using Jinja syntax provided by Flask, each template is extending the layout.html in **title** tag, **main** tag and the part of navbar containing references to other templates (in order to mark the page we are currently in).  

- ## index.html

As any other template, extends the layout.html in three blocks - **block title**, **block currenttab**, **block main**. 

This page contains some information about me, has link in buttons to my LinkedIn and GitHub accounts as well as the button to open the message to send on my e-mail.

The page is divided in shaded banner with an image(hero) in the upper part, and the section divided in columns on the bottom - one is having the "About me" section, the other is having the buttons to reach me out. I've used both Bulma and styles.css for that reason.

- ## projects.html

Contains the information about projects I have done so far. The upper part of page is a shaded banner with an image and the lower party is a section separated to columns containing boxes of information with both the descriptions and images of my work.

- ## experience.html

Contains the information about my work experience. The background of the page consists of a banner with a shaded image and the lower section containing another image that is shaded as well. The information of my workplaces and experiences as well as related photos to it are contained in **card** class provided by Bulma CSS Framework. Of course, I have customized some parts with my styles.css file.

- ## resume.html

Includes the shaded gif background at the top of the page as well as the box container with my CV in it. As well as everything else, I have made the embedded PDF container responsive the size changes.

- ## recommendations.html

This page includes the recommendations I have been given so far. At the top I have used a banner with a shaded image, and below I have divided the section into tiles with the help of Bulma and placed the Bulma's media objects customized by styles.css to fit the purpose. Moreover, each tile contains the button with references to contact the mentioned persons. 

- ## whygimilov.html

Brief page containing my inspiration for my nickname. The background is a shaded gif.



# Responsiveness 

It's worth mentioning that I have placed much efforts to optimize the webpage to be as responsive as possible. It worked well in my tests conducted on my phone. Many times I sized the various objects using the vw and vh reference etc. 
