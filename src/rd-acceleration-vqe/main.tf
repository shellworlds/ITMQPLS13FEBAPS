resource "null_resource" "quantum" {
  provisioner "local-exec" {
    command = "echo quantum rd-acceleration-vqe"
  }
}
