// Simple Node.js client to test the API
const fetch = require('node-fetch');

async function testPrediction() {
    const url = 'http://localhost:8000/predict/overpotential';
    const data = { composition: 'Ni70Fe20Co10', temperature: 75 };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        console.log('Prediction result:', result);
    } catch (error) {
        console.error('Error:', error);
    }
}

testPrediction();
