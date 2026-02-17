package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
)

type Query struct {
    Composition string  `json:"composition"`
    Temperature float64 `json:"temperature"`
}

type Response struct {
    Overpotential  float64 `json:"overpotential"`
    CurrentDensity float64 `json:"current_density"`
    Confidence     float64 `json:"confidence"`
}

func main() {
    url := "http://localhost:8000/predict/overpotential"
    query := Query{Composition: "Ni70Fe20Co10", Temperature: 75.0}
    jsonData, _ := json.Marshal(query)

    resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer resp.Body.Close()

    var result Response
    json.NewDecoder(resp.Body).Decode(&result)
    fmt.Printf("Prediction: %+v\n", result)
}
