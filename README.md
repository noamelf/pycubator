# Pycubator

[![Join the chat at https://gitter.im/noamelf/pycubator][gitter-img]][gitter-site]

Live slides are at [pycubator.com][pyc]

Pycubator (Python Incubator) is a collection of slides and exercises for teaching Python.
These slides are meant to be used in a teacher-led classroom, but also, put a strong emphasis on student exploration and participation. 

It utilizes [RevealJS][rjs] to create stunning slides, that are actually written in Markdown and hence easy to use with source control, and the exercises uses [Jupyter notebooks][jn] to reduce the amount boilerplate code the students needs to write. 

Pycubator leading principles are:

-   Talk less, practice more.
-   Real world examples

## Running locally
-   Run `python3 build.py` script to generate the HTML files.
-   Run `python3 -m http.server` and open your browser!

## Contributing
-   Slides are at `content/slides/` and are in MD form so it's very easy to edit them.
-   Exercises are Jupyter (IPython) notebooks residing at `content/exercises`.
-   After making some changes follow [running locally](#running-locally)

## Contributors
* [Noam Elfanbaum](https://twitter.com/noamelf)
* [Udi Oron](https://twitter.com/nonZero)

---

[![This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License][cc-img]][cc-site]


[cc-img]: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
[cc-site]: http://creativecommons.org/licenses/by-sa/4.0/

[gitter-img]: https://badges.gitter.im/Join%20Chat.svg
[gitter-site]: https://gitter.im/noamelf/pycubator?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

[rjs]: https://github.com/hakimel/reveal.js/
[jn]: http://jupyter.org/
[pyc]: http://pycubator.com

