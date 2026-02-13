resource "null_resource" "quantum" {
  provisioner "local-exec" {
    command = "echo quantum project-finance-2.0"
  }
}
