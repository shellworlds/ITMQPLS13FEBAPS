resource "null_resource" "quantum" {
  provisioner "local-exec" {
    command = "echo quantum global-scale-model"
  }
}
