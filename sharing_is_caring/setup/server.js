const express = require('express');
const { URL } = require('url');
const bodyParser = require('body-parser');
const fs = require('fs');
const cookie = require('cookie');

const bot = require('./bot.js');

const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.render('index', {head: req.query.head, body: req.query.body});
});

app.get('/robots.txt', (req, res) => {
    res.sendFile(__dirname + '/views/robots.txt');
});

app.get('/s3cr3t_fl4g_K1udg3', (req, res) => {
    const currentDomain = req.hostname;
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

app.get('/submit', (req, res) => {
    res.sendFile(__dirname + '/views/submit.html');
});

app.get('/get_cookie', (req, res) => {
    try {
        const secret = encodeURIComponent(req.query.secret);
        res.setHeader('Set-Cookie', 'secret='+secret+'; Max-Age=60; Path=/; HttpOnly; SameSite=Lax');
    } catch (error) {}
    res.status(200).send('Done');
});

app.post('/submit', (req, res) => {
    const submittedURL = req.body.url;
    try {
        const submittedDomain = new URL(submittedURL).host;
        const currentDomain = req.headers.host;

        // Check if the submitted URL is from the same domain & port
        if (submittedDomain === currentDomain) {
            // Run bot.js to visit the submitted URL and create cookie
            bot.visit(submittedURL, 'http://'+currentDomain+'/');
            res.send('Bot script executed successfully.');
        } else {
            res.status(400).send('Error: Submitted URL is not from the same domain/port.');
        }
    } catch (error) {
        res.status(400).send('Error: Invalid URL format.');
    }
});

app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});
