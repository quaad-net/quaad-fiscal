const myURL = (document.baseURI).replace('test/', '')
//console.log(myURL + 'fiscal/posts/getcontainers')
const req = await fetch(myURL + 'fiscal/posts/getcontainers')
const res = await req.text()
const parser = new DOMParser()
const doc = parser.parseFromString(res, 'text/html')
const postContainer = doc.querySelector('.post-container')
document.querySelector('html').appendChild(postContainer)

document.querySelector('.post-date').textContent += ' ' + 'myDate'
document.querySelector('.post-title').textContent += ' ' + 'myTitle'
document.querySelector('.post-description').textContent += ' ' + 'myDescription'
document.querySelector('.post-post').textContent += ' ' + 'myPost'


