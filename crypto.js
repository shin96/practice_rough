const crypto = require('crypto');
const algorithm = 'aes-256-ctr';
const password = 'tL9M3ah5MdUo6wkg1IKqSZRquoPl1V3N';

function encrypt(text, cipher = crypto.createCipher(algorithm, password), encoding = 'hex') {
    let crypted = cipher.update(text, 'utf8', encoding);
    crypted += cipher.final(encoding);
    console.log(crypted, "i am in crypted:")
    return crypted;
}

function decrypt(text, decipher = crypto.createDecipher(algorithm, password), encoding = 'hex') {
    let dec = decipher.update(text, encoding, 'utf8');
    dec += decipher.final('utf8');
    console.log(dec, "in dec")
    return dec;
}
encrypt("x1618555150818")
// decrypt("a9c9874adb97bbabbba79788d775")
// var mcache = require('memory-cache');
// var cache = (duration) => {
//     let key = req.url;
//     let cachedBody = mcache.get(key);
//     app.log(cachedBody);
// }