resource "null_resource" "quantum" {
  provisioner "local-exec" {
    command = "echo quantum talent-and-ip"
  }
}
