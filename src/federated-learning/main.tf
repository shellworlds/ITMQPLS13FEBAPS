resource "null_resource" "quantum" {
  provisioner "local-exec" {
    command = "echo quantum federated-learning"
  }
}
