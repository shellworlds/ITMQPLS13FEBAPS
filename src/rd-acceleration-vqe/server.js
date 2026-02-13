const express = require('express');
const app = express();
app.get('/quantum', (req, res) => {
    res.json({ branch: "rd-acceleration-vqe", status: "running" });
});
app.listen(3000, () => console.log('Listening on 3000'));
