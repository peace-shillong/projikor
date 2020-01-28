//https://www.freecodecamp.org/news/the-ultimate-guide-to-web-scraping-with-node-js-daa2027dcd3/

// npm i request cheerio request-promise-native
const rp = require('request-promise-native'); // requires installation of `request`
const cheerio = require('cheerio');

const url = 'https://mobile.facebook.com/groups/367491087209820?refid=27';//'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States';

rp(url)
  .then(function(html){
    //success!
    console.log(html);
    //console.log($('big>', html).length);
    //console.log($('big>', html));

  })
  .catch(function(err){
    //handle error
  });