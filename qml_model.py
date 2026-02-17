import tensorflow as tf
import numpy as np
import json
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
x_train = np.random.rand(500, 10)
y_train = np.random.rand(500, 1)

# Build a simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train
history = model.fit(x_train, y_train, epochs=20, batch_size=32, verbose=0, validation_split=0.2)

# Plot loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title("QML Surrogate Model Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.legend()
plt.savefig("qml_loss.png")

# Save model summary as JSON
summary = {
    "layers": [64, 64, 1],
    "activation": "relu",
    "optimizer": "adam",
    "loss": "mse",
    "epochs": 20,
    "final_train_loss": float(history.history['loss'][-1]),
    "final_val_loss": float(history.history['val_loss'][-1])
}
with open("qml_model_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("QML model training complete.")
