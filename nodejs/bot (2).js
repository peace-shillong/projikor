// npm i request cheerio request-promise-native
const rp = require('request-promise-native'); // requires installation of `request`
const cheerio = require('cheerio');

function GetFbPosts(pageUrl) {
    const requestOptions = {
        url: pageUrl,
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
    };
    return rp.get(requestOptions).then( postsHtml => {
        const $ = cheerio.load(postsHtml);
        const timeLinePostEls = $('.userContent').map((i,el)=>$(el)).get();
        const posts = timeLinePostEls.map(post=>{
            return {
                message: post.html(),
                created_at: post.parents('.userContentWrapper').find('.timestampContent').html()
            }
        });
        return posts;
    });
}
/*
GetFbPosts('https://www.facebook.com/sai.lyngdoh').then(posts=>{
    // Log all posts
    for (const post of posts) {
        console.log(post.created_at,post.message);
    }
});*/

const url = 'https://www.facebook.com/sai.lyngdoh';//'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States';

rp(url)
  .then(function(html){
    //success!
    console.log(html);
  })
  .catch(function(err){
    //handle error
  });