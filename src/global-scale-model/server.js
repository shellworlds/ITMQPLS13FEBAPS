const express = require('express');
const app = express();
app.get('/quantum', (req, res) => {
    res.json({ branch: "global-scale-model", status: "running" });
});
app.listen(3000, () => console.log('Listening on 3000'));
