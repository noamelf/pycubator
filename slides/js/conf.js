// Full list of configuration options available at:
// https://github.com/hakimel/reveal.js#configuration
Reveal.initialize({
    controls: true,
    progress: true,
    history: true,
    center: true,

    transition: 'slide', // none/fade/slide/convex/concave/zoom

    // Optional reveal.js plugins
    dependencies: [{
        src: 'revealjs/lib/js/classList.js',
        condition: function () {
            return !document.body.classList;
        }
    }, {
        src: 'revealjs/plugin/markdown/marked.js',
        condition: function () {
            return !!document.querySelector('[data-markdown]');
        }
    }, {
        src: 'revealjs/plugin/markdown/markdown.js',
        condition: function () {
            return !!document.querySelector('[data-markdown]');
        }
    }, {
        src: 'revealjs/plugin/highlight/highlight.js',
        async: true,
        condition: function () {
            return true;
        },
        callback: function () {
            hljs.initHighlightingOnLoad();
        }
    }, {
        src: 'revealjs/plugin/zoom-js/zoom.js',
        async: true
    }, {
        src: 'revealjs/plugin/notes/notes.js',
        async: true
    }]
});