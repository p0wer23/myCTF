const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const cookie = require('cookie');

const app = express();
const port = 2999;

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/s3cr3t_fl4g_K1udg3', (req, res) => {
    const currentDomain = req.hostname;
    console.log(currentDomain)
    res.setHeader('Access-Control-Allow-Origin', currentDomain);
    res.setHeader('Access-Control-Allow-Credentials', true);

    try {
        const cookies = cookie.parse(req.headers.cookie || '');
        const secret = cookies['secret'];
        res.render('s3cr3t_fl4g_K1udg3', {secret: secret});
    } catch (error) {
        res.render('s3cr3t_fl4g_K1udg3', {secret: undefined});
    }
});

app.get('/get_cookie', (req, res) => {
    try {
        const secret = encodeURIComponent(req.query.secret);
        res.setHeader('Set-Cookie', 'secret='+secret+'; Max-Age=60; Path=/; HttpOnly; SameSite=Lax');
    } catch (error) {}
    res.status(200).send('Done');
});

app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});
