const express = require('express');
const app = express();
app.get('/quantum', (req, res) => {
    res.json({ branch: "grid-optimization-qaoa", status: "running" });
});
app.listen(3000, () => console.log('Listening on 3000'));
