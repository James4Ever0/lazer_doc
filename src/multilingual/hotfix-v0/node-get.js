'use strict';

const { JSDOM } = require('jsdom');

const options = {
  resources: 'usable',
  runScripts: 'dangerously',
};

JSDOM.fromFile('index.html', options).then((dom) => {
  console.log(dom.window.document.body.textContent.trim());

  setTimeout(() => {
    console.log(dom.window.document.body.textContent.trim());
  }, 5000);
});

 // console output
 // abc
 // 123
