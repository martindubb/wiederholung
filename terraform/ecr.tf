resource "aws_ecr_repository" "myecr" {
  name                 = "my-flask-app"
  force_delete         = true
  image_tag_mutability = "MUTABLE"
}

